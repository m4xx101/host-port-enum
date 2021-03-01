# host-port-enum

Simple yet fast host discovery tool plus port scanner, give input IP of current system, it discover all host for /16,/24 subnet mask as defined also it launch port scan against it withe specified range of port and also enumrate service running on open ports.

# Usage
```sh
┌──(m4xx㉿m4xx)-[~/]
└─$ python3 host-port-enum.py -h

██╗  ██╗ ██████╗ ███████╗████████╗   ██████╗  ██████╗ ██████╗ ████████╗   ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████║██║   ██║███████╗   ██║█████╗██████╔╝██║   ██║██████╔╝   ██║█████╗█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██╔══██║██║   ██║╚════██║   ██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝███████║   ██║      ██║     ╚██████╔╝██║  ██║   ██║      ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ By m4xx
usage: host-port-enum.py [-h] [-ip IP] [-p PORT] [-r RANGE] [-t THREAD]

optional arguments:
  -h, --help            show this help message and exit
  -ip IP, --ipAddress IP
                        Current System IP Address
  -p PORT, --port PORT  Port range
  -r RANGE, --range RANGE
                        Scanning range Example: /16,/24
  -t THREAD, --thread THREAD
                        Threads Counts
```

# Output
```sh
┌──(m4xx㉿m4xx)-[~/]
└─$ python3 host-port-enum.py -ip 192.168.68.106 -p 1-65535 -r /16 -t 200

██╗  ██╗ ██████╗ ███████╗████████╗   ██████╗  ██████╗ ██████╗ ████████╗   ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████║██║   ██║███████╗   ██║█████╗██████╔╝██║   ██║██████╔╝   ██║█████╗█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██╔══██║██║   ██║╚════██║   ██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝███████║   ██║      ██║     ╚██████╔╝██║  ██║   ██║      ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ By m4xx

==================================================

[!] Starting Host Discovery For: 192.168.0.0/16

==================================================

[+]  192.168.68.102  Host is alive on the network
[+]  192.168.68.103  Host is alive on the network
[+]  192.168.68.104  Host is alive on the network
[+]  192.168.68.106  Host is alive on the network
[+]  192.168.68.107  Host is alive on the network
[+]  192.168.68.108  Host is alive on the network
[+]  192.168.68.109  Host is alive on the network
[+]  192.168.68.111  Host is alive on the network
[+]  192.168.1.5  Host is alive on the network


====================================================

[!]  Scanning Port for range 1-65535 on all live hosts

====================================================

Discovered port 7000 running bbs on 192.168.68.101 
Discovered port 53 running domain on 192.168.68.1 
Discovered port 7100 running font-service on 192.168.68.101 
Discovered port 6379 running redis on 192.168.68.106 
Discovered port 5432 running postgresql on 192.168.68.106 
```
