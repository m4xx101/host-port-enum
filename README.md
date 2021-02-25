# host-port-enum

Simple yet fast host discovery tool plus port scanner, give inpute IP of current system, it discover all host for /16 subnet and launch port scan against it.

# Usage
```sh
python host-port-enum.py <Current-System-IP> <Port-Range-To-Scan>
Example: python host-port-enum.py 192.168.29.1 1-65535
```

# Output
```sh
PS M:\> python3 .\host-port-enum.py 192.168.29.1 1-65535

==================================================

[!] Starting Host Discovery For:  192.168.29.0/16

==================================================

[+]  192.168.29.57  Host is alive on the network
[+]  192.168.29.1  Host is alive on the network
[+]  192.168.29.237  Host is alive on the network


====================================================

[!]  Scanning Port for range 1-65535 on all live hosts

====================================================

Discovered port 1900 running ssdp on 192.168.29.1
Discovered port 7 running echo on 192.168.29.237
Discovered port 9 running discard on 192.168.29.237
Discovered port 13 running daytime on 192.168.29.237
Discovered port 17 running qotd on 192.168.29.237
Discovered port 19 running chargen on 192.168.29.237
Discovered port 135 running epmap on 192.168.29.237
Discovered port 139 running netbios-ssn on 192.168.29.237
Discovered port 445 running microsoft-ds on 192.168.29.237
```
