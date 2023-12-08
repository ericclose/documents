## LAN IP

```bash
uci set network.lan.ipaddr="192.168.2.1"
uci commit network
/etc/init.d/network restart
```

## PPPoE internet connection

```bash
vim /etc/config/network
```

```config
config interface 'wan'
        option device 'eth1'
        option proto 'pppoe'
        option username 'username'
        option password 'password'
        option peerdns '0'
        list dns '223.5.5.5'
        list dns '223.6.6.6'

config interface 'wan6'
        option device 'eth1'
        option proto 'dhcpv6'
```

```bash
/etc/init.d/network restart

opkg update
```

## To install USB drivers manually

```bash
# Install the USB storage package (all USB versions)
opkg install kmod-usb-storage

# Install USB 3.0 drivers
opkg install kmod-usb3
insmod xhci-hcd

# To install support for UASP aka USB Attached SCSI (supported by many USB drives and drive enclosures, especially if USB 3.0. It enhances performance if it's supported by both the drive and the host controller in your device)
opkg install kmod-usb-storage-uas

# This will download the driver to use exFAT, there are currently no tools in OpenWrt to format/check exFAT
opkg install kmod-fs-exfat
opkg install libblkid1
```

## Reference

* [OpenWrt Wiki - PPPoE internet connection](https://openwrt.org/docs/guide-user/network/wan/wan_interface_protocols#pppoe_internet_connection)
* [OpenWrt Wiki - OpenWrt as router device](https://openwrt.org/docs/guide-user/network/openwrt_as_routerdevice#command-line_instructions)
* [OpenWrt Wiki - Upstream DNS provider](https://openwrt.org/docs/guide-user/base-system/dhcp_configuration#upstream_dns_provider)
* [OpenWrt Wiki - Installing and troubleshooting USB Drivers](https://openwrt.org/docs/guide-user/storage/usb-installing#to_install_usb_drivers_manually)
* [OpenWrt Wiki - Filesystems](https://openwrt.org/docs/guide-user/storage/filesystems-and-partitions#set_up_exfat)
