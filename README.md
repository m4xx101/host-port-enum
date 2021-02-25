# host-port-enum

Simple yet fast host discovery tool plus port scanner, give inpute IP of current system, it discover all host for /16 subnet and launch port scan against it.

# Usage
```sh
python host-port-enum.py <Current-System-IP> <Port-Range-To-Scan>
Example: python host-port-enum.py 192.168.29.1 1-65535
```

# Output
```sh
PS M:\> python3 .\host-port-enum.py 192.168.29.1 1-200
==================================================

Starting Scanning: For 192.168.29.0/16

==================================================

[+] 192.168.29.1 Host is alive on the network
[+] 192.168.29.57 Host is alive on the network
[+] 192.168.29.237 Host is alive on the network

==================================================

Port scanning in progress....

==================================================

Discovered open port running http on 192.168.29.1
Discovered open port running echo on 192.168.29.237
Discovered open port running discard on 192.168.29.237
Discovered open port running daytime on 192.168.29.237
Discovered open port running qotd on 192.168.29.237
Discovered open port running chargen on 192.168.29.237
Discovered open port running epmap on 192.168.29.237
Discovered open port running netbios-ssn on 192.168.29.237
```
