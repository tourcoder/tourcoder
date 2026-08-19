#!/usr/bin/env python3
"""
从 Git 历史生成 Hugo 历史版本页面。

在 `hugo` 命令之前运行。它会：
  1. 遍历 TRACK 里的 section，对每个 .md 文件读取完整 commit 历史
  2. 用 `git show <hash>:<path>` 还原每个历史版本的原文
  3. 写入 content/rev/... （构建产物，应加入 .gitignore）
  4. 同时写出 data/history.json，供当前文章页渲染「修改记录」列表

所有时间统一换算成 TZ 指定的时区后再写出。

URL 形态：
  正文     /文章slug/
  历史版本 /rev/文章slug/20240501-1230/

用法：
    if [ "$(git rev-parse --is-shallow-repository)" = "true" ]; then git fetch --unshallow; fi
    python3 scripts/build_revisions.py
    hugo --minify
"""

import json
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# ---------------------------------------------------------------- 配置
CONTENT = Path("content")
REV_DIR = CONTENT / "rev"          # 历史版本页输出目录
DATA_FILE = Path("data/history.json")
TRACK = ["blog"]                   # 需要版本历史的 section
MAX_REVISIONS = 0                  # 每篇最多保留几个历史版本，0 = 不限
TZ = ZoneInfo("Asia/Singapore")    # 输出时间统一换算到这个时区
# ------------------------------------------------------------------


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout


def commits_for(path: Path):
    """返回 [(hash, iso_date, subject, 该 commit 里的文件路径), ...]，新 → 旧。"""
    raw = git(
        "log", "--follow", "--name-only",
        "--format=%x00%H%x1f%aI%x1f%s", "--", str(path),
    )
    result = []
    for block in raw.split("\x00"):
        lines = [ln for ln in block.splitlines() if ln.strip()]
        if not lines:
            continue
        head, files = lines[0], lines[1:]
        commit_hash, date, subject = head.split("\x1f")
        # --follow 下文件可能被重命名过，取该 commit 中的实际路径
        result.append((commit_hash, date, subject, files[-1] if files else str(path)))
    return result


# 兼容 YAML(---) 与 TOML(+++) front matter，容忍 BOM 与 \r\n
FM_PATTERNS = (
    re.compile(r"\A\ufeff?---\r?\n(.*?)\r?\n---\r?\n?", re.S),
    re.compile(r"\A\ufeff?\+\+\+\r?\n(.*?)\r?\n\+\+\+\r?\n?", re.S),
)


def split_front_matter(text: str):
    for pat in FM_PATTERNS:
        m = pat.match(text)
        if m:
            return m.group(1), text[m.end():]
    return "", text


def extract(front_matter: str, key: str, fallback: str = "") -> str:
    # 同时匹配 YAML 的 `key: v` 与 TOML 的 `key = "v"`
    m = re.search(rf'^{key}\s*[:=]\s*(.+)$', front_matter, re.M)
    return m.group(1).strip().strip('"\'') if m else fallback


def yaml_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def to_local(iso: str) -> str:
    """把 git 记录的时间（Codespaces / 网页端提交均为 UTC）换算成 TZ。"""
    return datetime.fromisoformat(iso).astimezone(TZ).isoformat()


def main() -> None:
    if REV_DIR.exists():
        shutil.rmtree(REV_DIR)

    index: dict[str, list] = {}

    for section in TRACK:
        section_dir = CONTENT / section
        if not section_dir.exists():
            continue

        for source in sorted(section_dir.rglob("*.md")):
            key = str(source.relative_to(CONTENT))          # blog/my-post.md
            stem = key[:-3]                                 # blog/my-post
            # leaf bundle: blog/my-post/index.md -> blog/my-post
            if stem.endswith("/index") or stem.endswith("/_index"):
                stem = stem.rsplit("/", 1)[0]

            # 对齐 config.toml 里的 [permalinks] blog = "/:slug"
            current_fm, _ = split_front_matter(source.read_text(encoding="utf-8"))
            page_slug = extract(current_fm, "slug") or stem.rsplit("/", 1)[-1]
            live_url = f"/{page_slug}/"                     # 正文地址
            dir_slug = stem.replace("/", "--")              # 仅用于临时文件目录名

            history = commits_for(source)
            if len(history) < 2:
                continue  # 只有初版，没有「历史」可言

            entries = []
            used_stamps: set[str] = set()
            # history[0] 是最新一次提交，其内容 == 当前页面，跳过
            older = history[1:]
            if MAX_REVISIONS:
                older = older[:MAX_REVISIONS]

            for commit_hash, iso_date, subject, path_then in older:
                iso_date = to_local(iso_date)

                try:
                    old_text = git("show", f"{commit_hash}:{path_then}")
                except subprocess.CalledProcessError:
                    continue

                fm, body = split_front_matter(old_text)
                title = extract(fm, "title", page_slug)
                author = extract(fm, "author", "")

                # 2024-05-01T12:30:45+08:00 -> 20240501-1230
                stamp = iso_date[:16].replace("-", "").replace("T", "-").replace(":", "")
                if stamp in used_stamps:   # 同一分钟内多次提交，退化到秒
                    stamp = iso_date[:19].replace("-", "").replace("T", "-").replace(":", "")
                if stamp in used_stamps:   # 极端情况：同一秒
                    stamp = f"{stamp}-{commit_hash[:6]}"
                used_stamps.add(stamp)

                rev_url = f"/rev/{page_slug}/{stamp}/"

                dest = REV_DIR / dir_slug / f"{stamp}.md"
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(
                    "---\n"
                    f"title: {yaml_escape(title)}\n"
                    f"date: {iso_date}\n"
                    "type: revision\n"
                    f"url: {yaml_escape(rev_url)}\n"
                    f"canonical: {yaml_escape(live_url)}\n"
                    f"rev_hash: {commit_hash[:8]}\n"
                    f"rev_subject: {yaml_escape(subject)}\n"
                    f"author: {yaml_escape(author)}\n"
                    "_build:\n"
                    "  list: never\n"
                    "---\n\n" + body,
                    encoding="utf-8",
                )

                entries.append({
                    "date": iso_date,
                    "url": rev_url,
                    "subject": subject,
                    "hash": commit_hash[:8],
                })

            if entries:
                index[key] = entries

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    pages = sum(len(v) for v in index.values())
    print(f"生成 {pages} 个历史版本页面，覆盖 {len(index)} 篇文章")


if __name__ == "__main__":
    main()