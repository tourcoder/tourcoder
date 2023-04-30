---
title: "记录一次 App 审核"
slug: appreviewer-of-apple-sucks
author: "Bin Hua"
lastmod: 2020-08-13 09:11:45
date: 2018-02-08 07:25:08
tags: ["Apple", "App", "应用审核"]
---

最近被 Apple 的 App 审核给搞惨了，过程也让我对 Apple 感到失望，很多情况体现出了这些审核人员极度不负责，极度的敷衍了事。就拿一个具有代表性的 App 来说吧。

这个 App 是一个简单的图文编辑器，功能就是输入文字插入图片，然后将这些内容导出成一张图片，很简单，但就是这么一个简单的 App 却被审核人员拒绝了四次。

**1.0 版本**

只拒绝了一次，拒绝的理由是该应用太简单了，没有使用价值，没办法，增加了了数据库保存的功能，再次提交审核，没有什么问题，正常上线。

**1.1 版本**

我发现 1.0 版本中有一个文字编辑的 bug，我做了下修复，提交，但被拒绝了，拒绝的理由如下

```
2018年2月7日 上午7:48
发件人 Apple
Guideline 2.3.7 - Performance - Accurate Metadata
Your app name or subtitle to be displayed on the App Store includes keywords or descriptors, which are not appropriate for use in these metadata items.
Specifically, the following words in your app name or subtitle are considered keywords or descriptors:

一款简单的图文编辑器，可将内容导出一张图片，简单容易使用

Next Steps
To resolve this issue, please revise your app name or subtitle to remove any keywords and descriptors from all localizations of your app. Keywords can be entered in the Keywords field in iTunes Connect to be used as search terms for your app.

Resources
For information on how to revise your app name, please review Renaming a Project or App.
For information on changing the app name and other metadata in iTunes Connect, please review the View and edit app information page.
For resources on selecting a memorable and unique app name and subtitle, you may want to review the App Store Product Page information available on the Apple developer portal.
```

考虑到本应用已经有一个在线的版本，名字和内容是没有问题的，出问题的应该就是 subtitle(副标题) 了，但我的副标题正是我 App 功能的准确描述，费解，随即在后台回复了他们

```
2018年2月7日 上午9:14
发件人 ****
Which keywords in my subtitle is not allowed? `一款简单的图文编辑器，可将内容导出一张图片，简单容易使用` is the correct description of this app in Chinese, can you find some one who knows chinese, he may tell you that.
```

并且我还将副标题改成了 一款简单的图文编辑器，并且可以将编辑的内容导出成一张图片，并且告之了他们，但是让我不高兴事情来了，他们再次拒绝了这个 App，给出的理由显示出了他们的敷衍了事。

```
2018年2月8日 上午12:42
发件人 Apple
Hello,
Thank you for providing the information.
Regarding Guideline 2.3.7 - Performance - Accurate Metadata, the following words in your app name or subtitle are considered keywords or descriptors:

一款简单的图文编辑器，可将内容导出一张图片，简单容易使用

Specifically, the whole part contained keywords or descriptors.
To resolve this issue, it would be appropriate to revise your app name or subtitle to remove any keywords and descriptors from all localizations of your app. Keywords can be entered in the Keywords field in iTunes Connect to be used as search terms for your app.
We look forward to reviewing your resubmitted app.
Best regards,
App Store Review
```

他们再次拒绝这个 App 的理由还是之前副标题的问题，但素不知我已经更改了副标题，并且告之了他们，他们根本就没有仔细看，只是习惯性的拒绝了。于是我在后台进行了回复，并且附加了截图，我回复的语气显得不够友好。

```
2018年2月8日 上午1:02
发件人 ***
I had update the subtitle several hours ago, but you still give me the old subtitle, do you really review my app??????
Screen Shot 2018-02-08 at 1.00.57 AM.png
```

几乎在第一时间，他们回复了我。

```
2018年2月8日 上午2:56
发件人 Apple
2. 3 Performance: Accurate Metadata
Guideline 2.3.7 - Performance - Accurate Metadata

Your app name or subtitle to be displayed on the App Store includes keywords or descriptors, which are not appropriate for use in these metadata items.
Specifically, the following words in your app name or subtitle are considered keywords or descriptors:

一款简单的图文编辑器，并且可以将编辑的内容导出成一张图片

Next Steps
To resolve this issue, please revise your app name or subtitle to remove any keywords and descriptors from all localizations of your app. Keywords can be entered in the Keywords field in iTunes Connect to be used as search terms for your app.

Resources
For information on how to revise your app name, please review Renaming a Project or App.
For information on changing the app name and other metadata in iTunes Connect, please review the View and edit app information page.
For resources on selecting a memorable and unique app name and subtitle, you may want to review the App Store Product Page information available on the Apple developer portal.
```

和第一次一样，但只是把理由改成了我更改后的副标题，看来他们是跑去看了下我最新的副标题，他们的这波操作让我觉得有点恶心。最后我把这些内容打包，发了邮件给他们的 CEO，并且在 Hacker News 上发了一篇吐槽。

最后的情况，考虑到这只是一个内部用的 App，我并没有给它做 ASO 的打算，所以我删除了副标题的内容，并且在后台通知他们，也就是过了一个多小时，我收到邮件，App 通过审核，已经上线。

呵呵，App Reviewer of Apple Sucks!