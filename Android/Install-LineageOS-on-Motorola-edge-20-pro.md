# Edge S Pro 刷入 Official LineageOS 20 教程

本文将指引您将 Edge S Pro 刷入开源社区的 LineageOS 20 系统，本文将涵盖一些常见问题的 workaround。

> 本文内容遵循 署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0) 协议
> 
> 本文永久链接是: [https://github.com/ericclose/documents/blob/master/Android/Install-LineageOS-on-Motorola-edge-20-pro.md](https://github.com/ericclose/documents/blob/master/Android/Install-LineageOS-on-Motorola-edge-20-pro.md)

## 目录

- [Edge S Pro 刷入 Official LineageOS 20 教程](#edge-s-pro-刷入-official-lineageos-20-教程)
  - [目录](#目录)
  - [前情提要](#前情提要)
    - [USB 驱动的安装](#usb-驱动的安装)
    - [配置 ADB 的环境变量](#配置-adb-的环境变量)
    - [基础常识](#基础常识)
    - [解锁 bootloader](#解锁-bootloader)
    - [重要分区的备份](#重要分区的备份)
  - [固件的下载及刷写](#固件的下载及刷写)
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

> 1. **下载** LineageOS 19.1 配套的 recovery
> * LineageOS 19.1 recovery [下载地址](https://web.archive.org/web/20230707083131if_/https://gemmei.ftp.acc.umu.se/mirror/lineageos/full/pstar/20230606/boot.img)（最新版本的 LineageOS 20 的 `boot.img` 必须与 dtbo 和 vendor_boot 配套刷入才能正常使用，19.1 的则可以独立使用）
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

要想刷入第三方固件，**请确保您的设备已解锁 bootloader**

* Edge S Pro 官方 LineagOS 刷机包下载：
  
  * [LineageOS 链接](https://download.lineageos.org/devices/pstar/builds)
  
  > 下载 `dtbo.img`、`vendor_boot.img` 和 `lineage-20.0-*-nightly-pstar-signed.zip`，均选择最新的版本下载即可。

* LineageOS 的刷写：

```bash
# 刷入 dtbo 和 vendor_boot
# ⚠️本步骤为必要操作，否则 Lineage recovery 加载会很慢，且存在报错，功能异常问题
fastboot flash dtbo dtbo.img
fastboot flash vendor_boot vendor_boot.img

# 刷入 boot（将会替换官方 recovery 为 Lineage recovery）
fastboot flash boot boot.img

# 重启设备至 recovery 模式
fastboot reboot recovery

# 为确保 A/B 分区一致（分区不一致容易出错，甚至变砖），建议刷入 copy-partitions*.zip
# copy-partitions*.zip 下载地址：https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip
# 将手机重启进入 recovery 模式，「Apply Update 应用更新」→「Apply from ADB 通过adb侧载更新」
# 电脑执行命令刷入 copy-partitions*.zip：
adb sideload copy-partitions*.zip

# ⚠️经过上述步骤后请将设备再次重启至 recovery 模式（「Advanced 高级」→「Reboot to Recovery 重启至 recovery」）
#  「Apply Update 应用更新」→「Apply from ADB 通过adb侧载更新」
# 电脑执行命令刷入 LineageOS：
adb sideload lineage-20.0-*-nightly-pstar-signed.zip

# 刷入系统之后，清进行格式化操作，完成后设备就可以开机进系统了
# 「Factory Reset 工厂格式化」→「Format data/factory reset 格式化数据/工厂格式化」

# ------------------------------------------以下为可选操作--------------------------------------------------

# Gapps
# 如果需要刷入 Gapps，建议刷入 MindTheGapps
# MindTheGapps 下载链接（请根据您刷入系统的 Android 版本进行选择，如本文 LineageOS 20 对应 Android 13）： 
# https://androidfilehost.com/?w=files&flid=322935
# 刚刷完 LineageOS 刷机包，得再先重启至 recovery 一次（否则可能遇到分区挂载失败，刷写报错）
# 刷入方法一样是通过 adb sideload：
adb sideload MindTheGapps-13.0.0-arm64-*.zip

# Magisk
# 下载链接: https://github.com/topjohnwu/Magisk/releases
# 版本的选择上，本设备的 LineageOS 20 目前不兼容 Magisk v26 的版本，如果刷入将会遇到电话、数据（IMEI 无显示）、相机（显示杂乱条纹）无法使用的问题
# 建议暂时使用 Magisk v25.2 的版本
# 维护者在 XDA 论坛明确声明，如果不遵循官方 Wiki 安装系统，或使用第三方组件（如 Magisk），不要期望能得到支持。所以即便反馈也无济于事
# 建议至少开机一次，设置密码等保护后再刷入，这样才能保证设备处于加密状态
# 刷入方式选择其中一种即可
## 刷入方式①（ADB 侧载）：
adb sideload Magisk*.apk
# -------------------------------------------------------------------
## 刷入方式②（fastboot 刷入修补后的 boot.img）：
# 手机先安装 Magisk*.apk，打开后「Install 安装」→「Select and Patch a File 选择并修补文件」,
# 选择 LineageOS 网站下载得到的 boot.img，选择修补，完成后得到 magisk_patched*.img，将文件传至电脑
# 手机重启至 fastboot 模式，通过命令刷入 magisk_patched*.img：
fastboot flash --slot all boot magisk_patched*.img
```

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

<details open>
    <summary>本设备 LineageOS 20 目前存在的问题（点击以收起）</summary>

> 到目前为止，在最新的官方 LineageOS 构建 *20-20230704-NIGHTLY-pstar* 中发现了以下问题：
> 
> 1. 当显示设置中的**最低和峰值刷新率低于90Hz时，会出现肉眼可见的屏闪问题**（即使是反屏闪选项处于开启状态），手动将其调至为 90Hz 及以上即可。
> 
> 2. 设置 ➡️ Display ➡️ LiveDisplay ➡️ 显示模式，当设置为自动（默认值）或户外时。它将触发随机黑屏问题。关闭此功能即可解决问题
> 
> 3. 启用 USB 调试时，MTP 不工作（[更多细节和解决方法](https://forum.xda-developers.com/t/official-lineageos-20-for-the-moto-edge-20-pro.4594251/post-88716503)）。
> 
> 4. Magisk v26.1（没有任何模块）会破坏最新的官方 Lineage 20 构建，手机会冻结，几分钟后自动重启，相机显示杂乱条纹，电话和移动数据不工作（IMEI 没有显示）。但可与 Magisk v25.2 版正常搭配使用

</details>

<details open>
    <summary>关于 Google 账户锁的问题（点击以收起）</summary>

> 初次刷入 LineageOS 的系统不存在 Google 账户锁，可以跳过不登陆 Google 账户。但如果您已经登陆过 Google 账户，**未退出 Google 账户**或通过 recovery **抹除设备**（**而非通过系统设置恢复出厂设置**），再次使用带 Google 框架的固件则会触发 Google 账户锁（开机向导状态下，通知栏左上角有个 `🔒` 的标志，则为触发 Google 账户锁）。
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

* [Install LineageOS on Motorola edge 20 pro](https://wiki.lineageos.org/devices/pstar/install)

* [解锁 Bootloader 后先做的事 - 备份 CID 和 persist 分区](https://bbs.ixmoe.com/t/topic/27722)

* [Motorola 手机 Bootloader 解锁、改国际版方法](https://bbs.letitfly.me/d/1210)

* [重置保护 / 谷歌锁 Factory Reset Protection 的解除方法](https://bbs.letitfly.me/d/856)
