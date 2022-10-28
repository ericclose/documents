## SSH Local Forwarding

```bash
ssh root@x.x.x.x -L 127.0.0.1:80:192.168.0.1:80
```


```
SSH(1)                                             BSD General Commands Manual                                             SSH(1)

NAME
     ssh — OpenSSH remote login client
......
     -L [bind_address:]port:host:hostport
     -L [bind_address:]port:remote_socket
     -L local_socket:host:hostport
     -L local_socket:remote_socket
             Specifies that connections to the given TCP port or Unix socket on the local (client) host are to be forwarded to
             the given host and port, or Unix socket, on the remote side.  This works by allocating a socket to listen to either
             a TCP port on the local side, optionally bound to the specified bind_address, or to a Unix socket.  Whenever a con‐
             nection is made to the local port or socket, the connection is forwarded over the secure channel, and a connection
             is made to either host port hostport, or the Unix socket remote_socket, from the remote machine.

             Port forwardings can also be specified in the configuration file.  Only the superuser can forward privileged ports.
             IPv6 addresses can be specified by enclosing the address in square brackets.

             By default, the local port is bound in accordance with the GatewayPorts setting.  However, an explicit bind_address
             may be used to bind the connection to a specific address.  The bind_address of “localhost” indicates that the lis‐
             tening port be bound for local use only, while an empty address or ‘*’ indicates that the port should be available
             from all interfaces.
......
```

## Reference

* [SSH Tunneling: Examples, Command, Server Config](https://www.ssh.com/academy/ssh/tunneling-example)
