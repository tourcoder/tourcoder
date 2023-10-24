---
title: "Sublime Text 3"
slug: "sublime-text-3"
author: "Bin Hua"
date: 2016-08-20 06:50:24
tags: ["sublimetxt"]
---

Sublime Text 3 是我喜欢的编辑器，介绍下它在 macOS 下的安装和配置

**下载**

[Official Website](http://www.sublimetext.com/)

**Package**

- 打开 Sublime Text3

- 打开 Console: View->Console，或快捷键 

    ```
    Ctrl + `
    ```
    
- 把下面的代码贴进去，具体看 [PackageControl](https://packagecontrol.io/installation)

    ```
    import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
    ```

完成!

**PackageControl 被墙了**

无法直接安装包，需要做一下配置，如下图

![](/imgs/sublime-text-3-01.png)

进入到 `Package Control` 的 `Settings - User`，在里面增加

```
"channels":
	[
		"https://raw.githubusercontent.com/wilon/sublime/master/download/channel_v3.json"
	],
```

**Terminal**

- 按 `Command + Shift + P` 键，然后在弹出的输入框中输入 `Package Control: Install Package`

- 选择 Terminal

- 完成!

**SyncedSidebarBg**

让侧边栏和主窗口一样颜色

- 使用 `Package Control: Install Package`

- 搜索 `SyncedSidebarBg` 然后安装.

- 完成! 

**PrettyJson**

格式化 json 文件

- 使用 `Ctrl+Shift+p` 打开，搜索 `prettyjson`，安装完成即可

使用快捷键 `Ctrl+Alt+J` 即可格式化文件。

**更改字体**

- 打开 `Preferences->Settings-User`

- 写入配置文件 

```
{
    "font_face": "InputSansNarrow",
    "font_size": 13,
    "ignored_packages": ["Vintage"]
}
```

![](/imgs/sublime-text-3-02.png)

**保存全部文件**

进入 `preferences -> key bindings`，在 `user` 去加入如下内容

```
[
  { "keys": ["ctrl+shift+s"], "command": "save_all" }
]
```

**主题**

现在我使用的主题是 Base16，使用 `Package Control: Install Package`，输入 Base16，安装即可。

网上也很流行另外一个主题叫 Dracula，有兴趣的可以自己安装看看。

**清理相同行的文本**

在 sublime text 中，清理相同行的文本，先将其排序，然后再执行。`Edit -> Sort Lines` 排序，`^(.+)$[\r\n](^\1$[\r\n]{0, 1})+` 查找相同行。替换用 `\1`，建议后面用一个回车符。


**不记录已经打开的文件**

在 `Preferences.sublime-settings` 里面增加 

```
"hot_exit": false,
"remember_open_files": false
```

**VSCode 和 ST3 的设置**

有些东西的开发，我会用到 VSCode 和 ST3，我的配置如下

- VS Code user setting

    ```
    {
        "workbench.colorTheme": "Monokai",
        "editor.fontSize": 18,
        "editor.wordWrap": "on",
        "editor.lineHeight": 32,
        "editor.fontFamily": "iosevka, Menlo, Monaco, 'Courier New', monospace",
        "workbench.statusBar.visible": false,
        "workbench.activityBar.visible": false,
        "terminal.integrated.fontFamily": "iosevka",
        "terminal.integrated.fontSize": 16
    }
    ```

- Sublime text 3 Settings User

    ```
    {
      "color_scheme": "Packages/Base16 Eighties Dark Color Scheme/base16-eighties-dark.tmTheme",
      "font_face": "InputSansNarrow",
      "font_size": 13,
      "ignored_packages":
      [
          "Vintage"
      ],
      "caret_style": "phase",
      "ensure_newline_at_eof_on_save": true,
      "findreplace_small": true,
      "highlight_line": false,
      "hot_exit": false,
      "line_numbers": true,
      "line_padding_bottom": 5,
      "line_padding_top": 5,
      "remember_open_files": false,
      "show_definitions": false,
      "show_panel_on_build": false,
      "tab_size": 4,
      "tabs_small": false,
      "translate_tabs_to_spaces": true,
      "trim_trailing_white_space_on_save": true,
      "word_wrap": true
    }
    ```
