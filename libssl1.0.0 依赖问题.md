```bash
eric@kali:~$ sudo apt-get install -y mssql-server
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 mssql-server : Depends: libssl1.0.0 but it is not installable
E: Unable to correct problems, you have held broken packages.
```

You should be able to use any of the listed mirrors by adding a line to your /etc/apt/sources.list like this:

```bash
deb http://security.debian.org/debian-security jessie/updates main

sudo apt update
```
