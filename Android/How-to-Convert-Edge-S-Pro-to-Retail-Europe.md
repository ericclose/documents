# Edge S Pro 国行系统转换为欧洲零售版

本文将指引您将 Edge S Pro 国行系统转换为欧洲零售版的系统，并使其可以正常接收 OTA 更新。

至于我为什么要这么做？避开 Lenovo / Motorola 的远程施法只是其中一点 🤣。我最主要的理由是：欧洲地区的 [*GDPR* （通用数据保护条例）](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)，地表最强隐私保护法规了解一下。

> 本文内容遵循 署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0) 协议
> 
> 本文永久链接是: [https://ericclose.github.io/How-to-Convert-Edge-S-Pro-to-Retail-Europe.html](https://ericclose.github.io/How-to-Convert-Edge-S-Pro-to-Retail-Europe.html)

## 目录

- [Edge S Pro 国行系统转换为欧洲零售版](#edge-s-pro-国行系统转换为欧洲零售版)
  - [前情提要](#前情提要)
    - [USB 驱动的安装](#usb-驱动的安装)
    - [配置 ADB 的环境变量](#配置-adb-的环境变量)
    - [基础常识](#基础常识)
    - [解锁 bootloader](#解锁-bootloader)
    - [重要分区的备份](#重要分区的备份)
  - [固件的下载及刷写](#固件的下载及刷写)
  - [软件通道的转换操作](#软件通道的转换操作)
  - [FAQ](#faq)
  - [参考链接](#参考链接)

## 前情提要

### USB 驱动的安装

<details>
    <summary>点击以展开</summary>

* 请确保已正确**安装 Motorola USB 驱动**
  
  * [官网](https://en-gb.support.motorola.com/app/usb-drivers) 
  
  > 官方版本在缺乏某些运行环境（如 `Visual C++` 等）的情况下，Windows 上安装可能会报错，安装不上（且无有效提示信息）
  
  * [Motorola-USB-Drivers-win](https://github.com/ericclose/Motorola-USB-Drivers-win)
  
  > **推荐**，该版本无需依赖运行环境库也可以正常安装（仅需 Windows 10 v1607 及以上版本）。是我从 [Google USB 驱动](https://developer.android.com/studio/run/win-usb) 和 [Motorola Rescue and Smart Assistant](https://en-gb.support.motorola.com/app/answers/detail/a_id/158726) 提取而来，克隆或下载整个仓库，通过**以管理员模式运行** bat 脚本，即可完成驱动的安装）

</details>

---

### 配置 ADB 的环境变量

<details>
    <summary>点击以展开</summary>

* 配置 ADB 的环境变量的步骤
  
  * [ADB 下载](https://dl.google.com/android/repository/platform-tools_r33.0.3-windows.zip)
  
  * ADB 环境变量的配置方法：
    
    > Windows 10 及以上版本：按下 Win 键，键入 「environment variables」或『环境变量』，搜索预览结果选择**编辑系统环境变量**；『环境变量』→ 双击「系统变量」中的『PATH』→ 『新建』，在文本框输入 `adb.exe` **所在目录的绝对路径**，如『`D:\Program Files\platform-tools`』，最后保存即可。

</details>

---

### 基础常识

<details>
    <summary>点击以展开</summary>

* 知悉**启用 USB 调试**的方法
  
  > 『*Settings*』设置 →『*About Phone*』关于手机 → 快速连续点击『*Build number*』版本号，直至提示已启用开发者选项；
  > 
  > 『*Settings*』设置 →『*System*』系统 →『*Developer options*』开发者选项 →『*USB debugging*』USB 调试

* 知悉如何将手机**启动至 bootloader 模式**
  
  > * 方法 1：设备处于关机状态下，长按『电源键』&『音量 -』，直至设备启动至 bootloader 模式后即可松开按键
  > 
  > * 方法 2：设备启用 USB 调试之后，用数据线将手机与电脑连接，通过 cmd 执行命令 `adb reboot bootloader` 重启至 bootloader 模式

* 知悉如何将手机**启动至 recovery 模式**
  
  > * 方法 1：设备处于关机状态下，长按『电源键』&『音量 +』，直至设备启动至 recovery 模式后即可松开按键
  > 
  > * 方法 2：设备启用 USB 调试之后，用数据线将手机与电脑连接，通过 cmd 执行命令 `adb reboot recovery` 重启至 recovery 模式

</details>

---

### 解锁 bootloader

<details>
    <summary>点击以展开</summary>

* 请确保设备已经**解锁 bootloader**
  
  > 解锁 Motorola 设备的 bootloader 有以下影响，请自行决定是否解锁：
  > 
  > * 原则上意味着**放弃保修资格**
  > 
  > * 解锁操作将会**清除设备数据**
  > 
  > * 解锁 bootloader 后设备 **DRM 等级**将从 L1 **降低**至 L3（目前发现**欧版更新至 Android 13 又恢复成 L1**）
  > 
  > * 解锁后**设备启动**将会提示“**设备已解锁 bootloader**”
  
  * [解锁 bootloader - Motorola 官网](https://en-gb.support.motorola.com/app/standalone/bootloader/unlock-your-device-a)

</details>

---

### 重要分区的备份

<details open>
    <summary>点击以收起</summary>

* ⚠️ **备份**重要的分区
  
  * `cid`：用于分配 CPU ID、手机区域代码、bootloader 解锁标识符等。主管设备能刷入的固件
  
  * `persist`：主管出厂的一些数据，例如 IMEI、蓝牙，WIFI MAC 地址、设备 SN 等参数

> 1. **下载** Lineage recovery
> * Lineage recovery [下载地址](https://download.lineageos.org/devices/pstar/builds)（下载最新版本的 `boot.img` 即可）
> 2. 将手机**重启至 bootloader 模式**，通过命令**刷入 Lineage recovery**

```bash
# <boot.img_路径> 不需要手动填写，直接将 boot.img 拖至 cmd 窗口会自动填写路径
fastboot flash boot <boot.img_路径>
# 实例：fastboot flash boot D:\Downloads\boot.img
```

> 3. 将手机**重启至 recovery 模式**，通过 Lineage recovery（「*Advanced*」**高级** →「*Enable ADB*」**启用 ADB shell**），电脑**使用命令进行备份**：

```bash
# 访问 shell，shell 环境以 `pstar:/ #` 开头
adb shell

# /tmp 是临时挂载目录，重启会自动清除，我们将 cid 和 persist 暂时导出至 /tmp 目录
dd if=/dev/block/bootdevice/by-name/cid of=/tmp/cid
dd if=/dev/block/bootdevice/by-name/persist of=/tmp/persist
# 退出 shell 环境
exit

# 将导出的 cid 和 persist 所在的 tmp 目录整个导出，备份至电脑的目录
# 请根据自身情况，妥善选择备份至的电脑路径，如：D:\Downloads\
adb pull /tmp/ D:\Downloads\
```

</details>

---

## 固件的下载及刷写

* Edge S Pro / Edge 20 Pro / pstar 欧洲零售版（RETEU）固件下载：
  
  * [固件链接](https://mirrors.lolinet.com/firmware/motorola/pstar/official/RETEU/)
  
  > 选择最新的版本下载即可

* RETEU 固件的刷写：
  
  > 此处我们需要用到 `motorola_flash_xml` 工具（很多人喜欢用 [TinyFastbootScript](https://mirrors.lolinet.com/software/windows/TinyFastbootScript/) 刷机工具，感兴趣的可以自行去研究）协助我们生成 fastboot 刷写脚本，而本文使用的工具依赖于 Python。所以我们的操作如下：
  > 
  > 1. 首先[下载](https://www.python.org/downloads/)并安装 Python 最新版
  >    
  >    * ⚠️ 安装的时候，确认勾选「*Add `python.exe` to PATH*」**添加 `python.exe` 到 PATH** 的选项，其他保持默认即可。
  > 
  > 2. 克隆或下载 [motorola_flash_xml](https://gitlab.com/ThomasHastings/motorola_flash_xml) 整个仓库
  > 
  > 3. 将 RETEU 的固件 `*.zip` 解压到 `motorola_flash_xml.py` 所在的目录（即 `flashfile.xml` 与 `motorola_flash_xml.py` 处于同一目录）
  > 
  > 4. 通过 cmd 执行以下命令：
  > 
  > ```bash
  > # 将 cmd 的路径切换至 motorola_flash_xml.py 所在的目录，如：
  > cd /d D:\repo\motorola_flash_xml
  > 
  > # 生成刷写脚本：
  > python motorola_flash_xml.py
  > 
  > # 刷写 RETEU 固件：
  > flash_all.bat
  > ```

执行完上述操作之后，RETEU 的系统就刷写进去了。

---

## 软件通道的转换操作

修改软件通道之后，您的设备将可以正常接收欧洲零售版的 OTA 更新。操作方法如下：

1. 将手机重启至 bootloader 模式

2. 更改『*Software channel*』软件通道为 `reteu`
   
   设备处于 bootloader 模式下，cmd 键入命令：

```batch
fastboot oem config carrier reteu
```

您**仍需**要将设备**恢复出厂设置**之后，软件通道的修改才能生效

『*Software channel*』**软件通道 的查看**：

* 『*Settings*』设置 →『*About Phone*』关于手机 →『*Software channel*』软件通道

---

## FAQ

<details>
    <summary>关于回锁 bootloader 的问题（点击以展开）</summary>

> Motorola 零售机的 bootloader 有三种模式：
> 
> * `oem_locked`：bootloader 的出厂状态
> 
> * `flashing_unlocked`：解锁 bootloader 后的状态
> 
> * `flashing_locked`：通过命令回锁的状态。
> 
> **回锁**（`flashing_locked`）有以下影响：
> 
> * **回锁**不能恢复您的保修资格（因为 bootloader 状态与出厂不符），且并**不能恢复 DRM 等级**；
> 
> * 如果您刷的是**匹配地区的官方固件**（且**未经任何修改**，如未装 Magisk 等），**回锁**您**可能仍能正常启动**；
> 
> * 但如若刷了**其他区域的固件**或**第三方固件**，**回锁可能只会直接导致变砖**；
> 
> * **回锁**可能会导致您**无法通过官方的解锁方法再次解锁 bootloader**

</details>

<details>
    <summary>关于系统降级的问题（点击以展开）</summary>

> * Motorola 全部机型的 **Bootloader** 和**基带** (*Baseband Part*) 部分存在熔丝级防降级机制，刷入之后**很可能无法降级回许久未更新的国行系统**。
> 
> * 多数情况下，**基带版本降级**可能会导致**设备 IMEI 丢失**或**手机信号丢失**的情况，**更新版本后则可恢复正常**。

</details>

<details open>
    <summary>关于 Google 账户锁的问题（点击以收起）</summary>

> 初次刷入 RETEU 的系统不存在 Google 账户锁，可以跳过不登陆 Google 账户。但如果您已经登陆过 Google 账户，**未退出 Google 账户**或通过 recovery **抹除设备**（**而非通过系统设置恢复出厂设置**），再次使用 RETEU 固件则会触发 Google 账户锁（开机向导状态下，通知栏左上角有个 `🔒` 的标志，则为触发 Google 账户锁）。
> 
> 可以通过 Lineage recovery（「*Advanced*」**高级** →「*Enable ADB*」**启用 ADB shell**）使用命令抹除 `frp` 分区解决：
> 
> ```bash
> dd if=/dev/zero of=/dev/block/bootdevice/by-name/frp bs=512 count=1024
> ```
> 
> 抹除完 `frp` 分区后，请再进入**系统设置完成一次正常的恢复出厂设置**（否则您可能会遇到一些奇奇怪怪的问题，如无法通过 apk 安装软件等）

</details>

---

## 参考链接

* [解锁 Bootloader 后先做的事 - 备份 CID 和 persist 分区](https://bbs.ixmoe.com/t/topic/27722)

* [Motorola 手机 Bootloader 解锁、改国际版方法](https://bbs.letitfly.me/d/1210)

* [重置保护 / 谷歌锁 Factory Reset Protection 的解除方法](https://bbs.letitfly.me/d/856)