## 编译 OpenWrt

### 临时代理

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
export no_proxy=localhost,127.0.0.0/8,::1
```

### 编译准备

```bash
git config --global http.proxy http://127.0.0.1:7890

# Download and update the sources
git clone https://git.openwrt.org/openwrt/openwrt.git
cd openwrt
git pull

# Select a specific code revision
git branch -a
git tag
git checkout v21.02.3

# Package prerequisites
sudo dnf --setopt install_weak_deps=False --skip-broken install \
bash-completion bzip2 gcc gcc-c++ git make ncurses-devel patch \
rsync tar unzip wget which diffutils python2 python3 perl-base \
perl-Data-Dumper perl-File-Compare perl-File-Copy perl-FindBin \
perl-Thread-Queue

# Update the feeds
./scripts/feeds update -a
./scripts/feeds install -a

# Configure the firmware image and the kernel
make menuconfig
make -j $(nproc) kernel_menuconfig

# Build the firmware image
make -j $(nproc) defconfig download clean world
```

---

### Cleaning up

| > Cleaned components >  <br>v make argument v | Compiled binaries:  <br>firmware, kernel, packages | Toolchain  <br>(target-specific) | Build tools,  <br>tmp/ | Compiled  <br>config tools | .config | feeds, .ccache,  <br>downloaded source files |
| --------------------------------------------- | -------------------------------------------------- | -------------------------------- | ---------------------- | -------------------------- | ------- | -------------------------------------------- |
| clean                                         | x                                                  |                                  |                        |                            |         |                                              |
| targetclean                                   | x                                                  | x                                |                        |                            |         |                                              |
| dirclean                                      | x                                                  | x                                | x                      | x                          |         |                                              |
| config-clean                                  |                                                    |                                  |                        | x                          |         |                                              |
| distclean                                     | x                                                  | x                                | x                      | x                          | x       | x                                            |

```bash
# Nukes everything you have compiled or configured and also deletes all downloaded feeds contents and package sources. :!: In addition to all else, this will erase your build configuration <buildroot>/.config. Use only if you need a “factory reset” of the build system!
make distclean
```

---

```bash
[eric@fedora openwrt]$ find -name "*squashfs-kernel1.bin" | xargs sha1sum
79179bf256b0a3547050b8cec5915bb9cb98a4c7  ./build_dir/target-mipsel_24kc_musl/linux-ramips_mt7621/tmp/openwrt-ramips-mt7621-xiaomi_mi-router-ac2100-squashfs-kernel1.bin
79179bf256b0a3547050b8cec5915bb9cb98a4c7  ./bin/targets/ramips/mt7621/openwrt-ramips-mt7621-xiaomi_mi-router-ac2100-squashfs-kernel1.bin

[eric@fedora openwrt]$  find -name "*squashfs-rootfs0.bin" | xargs sha1sum
452f5b21313d0a6208b279e1d5200d67aad5627f  ./build_dir/target-mipsel_24kc_musl/linux-ramips_mt7621/tmp/openwrt-ramips-mt7621-xiaomi_mi-router-ac2100-squashfs-rootfs0.bin
452f5b21313d0a6208b279e1d5200d67aad5627f  ./bin/targets/ramips/mt7621/openwrt-ramips-mt7621-xiaomi_mi-router-ac2100-squashfs-rootfs0.bin

[eric@fedora openwrt]$ find -name "*.ipk" | grep dnsmasq | xargs sha1sum
6991dd0d5cab1f115448089367d2a058bbd42854  ./staging_dir/packages/ramips/dnsmasq_2.85-8_mipsel_24kc.ipk
6991dd0d5cab1f115448089367d2a058bbd42854  ./bin/packages/mipsel_24kc/base/dnsmasq_2.85-8_mipsel_24kc.ipk
```