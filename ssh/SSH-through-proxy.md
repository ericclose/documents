## SSH through proxy

* 当你使用的是 Windows 上的 Git Bash 时，输入如下命令即可通过代理 ssh 登录远程服务器：

```bash
ssh username@x.x.x.x -o "ProxyCommand=connect -H 127.0.0.1:7890 %h %p"
```

> * **注**：7890 为 clash 的 HTTP 代理端口

---

* 当你使用的是 Linux / macOS 的终端时，输入如下命令即可通过代理 ssh 登录远程服务器：

```bash
ssh username@x.x.x.x -o "ProxyCommand=nc -X connect -x 127.0.0.1:7890 %h %p"
```

Linux 用户可能需要自行安装 OpenBSD netcat，否则可能报错，此处以 Fedora 为例子：

```bash
# 查询提供 nc 命令的软件包（查询到 netcat 和 nmap-ncat）
dnf provides nc

# 卸载系统内的非 OpenBSD 版本 netcat
sudo dnf remove nmap-ncat

# 安装 OpenBSD netcat
sudo dnf install netcat
```

## Reference

* [Connect with SSH through a proxy](https://stackoverflow.com/questions/19161960/connect-with-ssh-through-a-proxy)
