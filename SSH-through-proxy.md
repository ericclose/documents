## SSH through proxy

* 当你使用的是 Windows 上的 Git Bash 时，输入如下命令即可通过代理：

```bash
ssh username@x.x.x.x -o "ProxyCommand=connect -H 127.0.0.1:7890 %h %p"
```

> * **注**：7890 为 clash 的 HTTP 代理端口

## Reference

* [Connect with SSH through a proxy](https://stackoverflow.com/questions/19161960/connect-with-ssh-through-a-proxy)
