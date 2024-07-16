1. Remove or disable the *WAN* and *WAN6* interfaces. On the *Network → Interfaces* page, **Edit** the *WAN* and *WAN6* interfaces to uncheck the *Bring up on boot* checkbox. Or just delete the interfaces.

2. *Network → Interfaces → Devices*, **Configure...**，添加 **Ethernet Adapter: "..."** 到 *Bridge ports*

3. *Network → Interfaces*, **Edit** the *LAN* interface，set the following items:
* *General Settings*
  
  * *IPv4 address*: upstream 路由器 DHCP 分配范围未使用的 IP
  
  * *IPv4 netmask*: upstream 路由器 DHCP 的掩码
  
  * *IPv4 gateway*: upstream 路由器的 LAN IP

* *Advanced Settings*
  
  * Use custom DNS servers: upstream 路由器的 LAN IP

* *DHCP Server*
  
  * *General Setup*
    
    * - [x] Ignore interface
  
  * *IPv6 Settings*
    
    * RA-Service: disabled
    
    * DHCPv6-Service: disabled
    
    * NDP-Proxy: disabled

4. *System→ Startup*，禁用以下服务：
* firewall

* dnsmasq

* odhcpd

5. 插拔网线，重启路由器
