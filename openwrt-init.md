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