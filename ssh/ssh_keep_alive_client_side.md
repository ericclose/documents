```bash
vim ~/.ssh/config
```

```bash
Host *
    ServerAliveInterval 240
    ServerAliveCountMax 2
```

```bash
man ssh_config
```

NAME

* ssh_config — OpenSSH client configuration file

DESCRIPTION

* *ServerAliveCountMax*

Sets the number of server alive messages (see below) which may be sent without [ssh(1)](https://manpages.debian.org/buster/openssh-client/ssh.1.en.html) receiving any messages back from the server. If this threshold is reached while server alive messages are being sent, ssh will disconnect from the server, terminating the session. It is important to note that the use of server alive messages is very different from `TCPKeepAlive` (below). The server alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by `TCPKeepAlive` is spoofable. The server alive mechanism is valuable when the client or server depend on knowing when a connection has become inactive.

The default value is 3. If, for example, `ServerAliveInterval` (see below) is set to 15 and `ServerAliveCountMax` is left at the default, if the server becomes unresponsive, ssh will disconnect after approximately 45 seconds.

* *ServerAliveInterval*

Sets a timeout interval in seconds after which if no data has been received from the server, [ssh(1)](https://manpages.debian.org/buster/openssh-client/ssh.1.en.html) will send a message through the encrypted channel to request a response from the server. The default is 0, indicating that these messages will not be sent to the server.

* *TCPKeepAlive*

Specifies whether the system should send TCP keepalive messages to the other side. If they are sent, death of the connection or crash of one of the machines will be properly noticed. This option only uses TCP keepalives (as opposed to using ssh level keepalives), so takes a long time to notice when the connection dies. As such, you probably want the `ServerAliveInterval` option as well. However, this means that connections will die if the route is down temporarily, and some people find it annoying.

The default is `yes` (to send TCP keepalive messages), and the client will notice if the network goes down or the remote host dies. This is important in scripts, and many users want it too.

To disable TCP keepalive messages, the value should be set to `no`. See also `ServerAliveInterval` for protocol-level keepalives.