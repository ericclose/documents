## 在`archiso`环境中使 SSH 允许 root 登录

默认情况下，ArchLinux 不允许使用 root 用户 SSH 连接。为了能使用 root 登录，你可以通过编辑`/etc/ssh/sshd_config` 来实现：

```bash
vim /etc/ssh/sshd_config
```

取消 `PasswordAuthentication yes` 的注释（即去掉 `#`）：

```conf
#PasswordAuthentication yes
```

之后启动`sshd`服务即可：

```bash
systemctl start sshd
```