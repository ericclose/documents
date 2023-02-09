## SSH through proxy

* 当你使用的是 Windows 上的 Git Bash 时，输入如下命令即可通过代理 ssh 登录远程服务器：

```bash
ssh username@x.x.x.x -o "ProxyCommand=connect -H 127.0.0.1:7890 %h %p"
```

> * **注**：7890 为 clash 的 HTTP 代理端口

---

* 当你使用的是 Linux 的终端(使用 nmap-ncat)时，输入如下命令即可通过代理 ssh 登录远程服务器：

```bash
ssh username@x.x.x.x -o "ProxyCommand=ncat --proxy 127.0.0.1:7890 --proxy-type http %h %p"
```

---

* 当你使用的是 Linux / macOS 的终端(使用 netcat-openbsd)时，输入如下命令即可通过代理 ssh 登录远程服务器：

```bash
ssh username@x.x.x.x -o "ProxyCommand=nc -X connect -x 127.0.0.1:7890 %h %p"
```

Linux 用户请确保只有一个 nc 命令程序，nmap-ncat 和 netcat-openbsd 的命令用法和选项不一致，此处以 Fedora 为例子：

```bash
# 查询提供 nc 命令的软件包（查询到 netcat 和 nmap-ncat，其中 netcat 为 openbsd 的版本，nmap-ncat 也提供 nc 程序）
dnf provides nc

# 卸载不想使用的 nc 程序的软件包
sudo dnf remove <package_name>
```

## Reference

* [Connect with SSH through a proxy](https://stackoverflow.com/questions/19161960/connect-with-ssh-through-a-proxy)
