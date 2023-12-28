---
title: "用 ElectronJS 开发应用"
slug: "make-an-app-by-using-electronjs"
author: "Bin Hua"
date: 2018-11-07 07:48:54
tags: ["iOS", "macOS", "App", "electron"]
draft: false
---

需要开发多桌面系统的应用，图省事，选择了 ElectronJS，因为时间关系，开发前没有细致的阅读文档，导致在开发的时候，查资料时间比较多。建议各位在用它做开发前，熟读它的文档。

**开发过程**

整个开发过程没有什么特殊的，基本可以看成用 NodeJS 开发一个网站。安装环境，初始化项目，根据文档接口和需求进行开发。

另外：我用的是 Javascript，也可以用 TypeScript。

**打包**

如果你只是想发布应用，直接打包即可，我用的是 electron-packager 这个打包库，下面是 package.json 文件的部分内容

```
{
  "private": true,
  "name": "Tourcoder",
  "productName": "Tourcoder",
  "version": "0.1.0",
  "description": "My blog",
  "bundleID": "com.tc.tourcoder",
  "main": "main.js",
  "author": {
    "name": "tourcoder",
    "email": "hello@tourcoder.com",
    "url": "https://tourcoder.com/"
  },
  "homepage": "https://tourcoder.com/",
  "scripts": {
    "start": "electron .",
    "mac": "electron-packager . --overwrite --platform=darwin --arch=x64 --icon=assets/images/appicon.icns --prune=true --out=out --osx-sign.identity='Developer ID Application: TOURCODER' --extend-info=assets/mac/Info.plist",
    "win": "electron-packager . --overwrite --platform=win32 --arch=ia32 --out=out --icon=assets/images/appicon.ico",
    "linux": "electron-packager . --overwrite --platform=linux --arch=x64 --out=out",
  },
  "devDependencies": {
    "electron": "^3.0.7",
    "electron-packager": "^12.2.0"
  }
}
```

**上传到 AppStore**

其实上面打包出来的应用就可以直接在 macOS 上使用，但我这里需要上传到 AppStore，ElectronJS 官网也有清楚的说明，但会遇到一些问题

1. 证书问题

开发者应用签名证书应该是有两个的，一个是 APP_KEY，一个是 INSTALLER_KEY，都是在 developer.apple.com 创建。

2. 打包后的文件，找不到 icns 文件

这个问题比较普遍，应该如下操作，先准备一个 1024x1024 大小的 logo，然后，在 macOS 的终端中，执行下面的命令

```
mkdir icon.iconset
sips -z 16 16     1024.png --out icon.iconset/icon_16x16.png
sips -z 32 32     1024.png --out icon.iconset/icon_16x16@2x.png
sips -z 32 32     1024.png --out icon.iconset/icon_32x32.png
sips -z 64 64     1024.png --out icon.iconset/icon_32x32@2x.png
sips -z 128 128   1024.png --out icon.iconset/icon_128x128.png
sips -z 256 256   1024.png --out icon.iconset/icon_128x128@2x.png
sips -z 256 256   1024.png --out icon.iconset/icon_256x256.png
sips -z 512 512   1024.png --out icon.iconset/icon_256x256@2x.png
sips -z 512 512   1024.png --out icon.iconset/icon_512x512.png
sips -z 1024 1024 1024.png --out icon.iconset/icon_512x512@2x.png
iconutil -c icns icon.iconset
rm -R icon.iconset
```

使用生成后的 icns 文件即可.

**上传的文件格式**

应该是上传 .pkg 文件或者将 .app 压缩成 zip 包，然后上传，我使用 Application Loader 上传。

**上传文件的制作**

按 ElectronJS 官方的教程打包是有问题的，而且非常啰嗦，打包需要准备几个文件 Info.plist，child.plist，parent.plist 和 loginhelper.plist，具体内容可以看官方说明。创建一个 .sh 文件

```
# 应用名称
APP="Tourcoder"
# 应用路径
APP_PATH="./out/$APP-mas-x64/$APP.app"
# 生成安装包路径
RESULT_PATH="./out/$APP.pkg"
# 开发者应用签名证书
APP_KEY="3rd Party Mac Developer Application: Tourcoder (1221212)"
INSTALLER_KEY="3rd Party Mac Developer Installer: Tourcoder (1221212)"
# 框架路径
FRAMEWORKS_PATH="$APP_PATH/Contents/Frameworks"
# 授权文件路径
CHILD_PLIST="./assets/mac/child.plist"
PARENT_PLIST="./assets/mac/parent.plist"
LOGINHELPER_PLIST="./assets/mac/loginhelper.plist"

codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Electron Framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libffmpeg.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework/Versions/A/Libraries/libnode.dylib"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/Electron Framework.framework"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper.app/Contents/MacOS/$APP Helper"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper.app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper EH.app/Contents/MacOS/$APP Helper EH"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper EH.app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper NP.app/Contents/MacOS/$APP Helper NP"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$FRAMEWORKS_PATH/$APP Helper NP.app/"
codesign -s "$APP_KEY" -f --entitlements "$LOGINHELPER_PLIST" "$APP_PATH/Contents/Library/LoginItems/$APP Login Helper.app/Contents/MacOS/$APP Login Helper"
codesign -s "$APP_KEY" -f --entitlements "$LOGINHELPER_PLIST" "$APP_PATH/Contents/Library/LoginItems/$APP Login Helper.app/"
codesign -s "$APP_KEY" -f --entitlements "$CHILD_PLIST" "$APP_PATH/Contents/MacOS/$APP"

codesign -s "$APP_KEY" -f --entitlements "$PARENT_PLIST" "$APP_PATH"

productbuild --component "$APP_PATH" /Applications --sign "$INSTALLER_KEY" "$RESULT_PATH"
```

注意不要弄错步骤，执行这个文件将生成的 .pkg 文件上传即可。