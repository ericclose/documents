## shadowsocks-qt5 编译安装全程

>首先说一下，编译安装 shadowsocks-qt5 之前，有一个依赖包（即 libQtShadowsocks）不在 Fedora 的仓库里，这就是为什么我们还需要编译安装 libQtShadowsocks 的原因。

### libQtShadowsocks 依赖

* qt5-devel
* botan2-devel
* cmake
* gcc-c++

### 安装 libQtShadowsocks 所需要的依赖

```bash
sudo dnf -y install qt5-devel botan2-devel cmake gcc-c++
```

### 编译安装 libQtShadowsocks

```bash
git clone https://github.com/ericclose/libQtShadowsocks.git
cd libQtShadowsocks
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make -j4
sudo make install
```

此处为什么不下载官方归档好的源码呢，详情点此[issue](https://github.com/shadowsocks/shadowsocks-qt5/issues/760#issuecomment-435806894)，本文为了方便自己编译，故根据这个issuse作出了仅有的少数改动，即可成功编译。

### shadowsocks-qt5 依赖

* cmake
* qt5-qtbase-gui
* qrencode-devel
* libQtShadowsocks （正是我们前面所编译安装的）
* zbar-devel
* libappindicator-devel

### 安装 shadowsocks-qt5 所需要的依赖

```bash
sudo dnf -y install cmake qt5-qtbase-gui qrencode-devel zbar-devel libappindicator-devel
```

### 编译安装 shadowsocks-qt5

```bash
curl -L https://github.com/shadowsocks/shadowsocks-qt5/archive/v3.0.1.tar.gz > shadowsocks-qt5-3.0.1.tar.gz
tar -xzvf shadowsocks-qt5-3.0.1.tar.gz
cd shadowsocks-qt5-3.0.1
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr
make -j4
sudo make install
```

到这里我们就完成了所有工作，你可以在应用列表里看到了，但是如果这时发现图标没有正常的显示，可以这么做。

```bash
sudo vim /usr/share/applications/shadowsocks-qt5.desktop
```

在 Icon=xxxx 这个添加上你下载好的图标的路径，如`Icon=/home/innovation/Pictures/icons/shadowsocks-qt5.svg`
[点此](https://icon-icons.com/descargaimagen.php?id=94122&root=1381/SVG/&file=shadowsocksqt5_94122.svg)下载svg图标。