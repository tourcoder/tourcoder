---
title: "Swift 中 NavigationController 的切换改变"
slug: "change-navigationcontroller-in-swift"
author: "Bin Hua"
date: 2019-05-29 05:08:30
tags: ["iOS", "swift", "CATransition", "pushviewcontroller", "popviewcontroller", "navigationcontroller", "代码示例"]
draft: false
---

最近在一个用 Swift 写的项目中，用到了 `NavigationController` 来进行界面的切换，即用到了 `pushViewController` 和 `popViewController`，众所周知，pushViewController 是从右向左载入新界面，而 popViewController 是从左向右退回返回到旧界面。那么是否有可能让它们的方向是相反的呢？

答案是可以，这里用到了 `CATransition`，直接上代码，pushViewController 部分

```
let newVC = NewVC()
let transition = CATransition()
transition.duration = 0.3
transition.type = .push
transition.subtype = .fromLeft
self.navigationController?.view.layer.add(transition, forKey: kCATransition)
self.navigationController?.pushViewController(newVC, animated: false)
```

从上面代码即可以看出将 profileVC 从左向右载入，那么 popViewController 用反方向即可

```
let transition = CATransition()
transition.duration = 0.3
transition.type = .push
transition.subtype = .fromRight
self.navigationController?.view.layer.add(transition, forKey: kCATransition)
self.navigationController?.popViewController(animated: false)
```
