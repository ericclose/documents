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
        option ipv6 'auto'

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
