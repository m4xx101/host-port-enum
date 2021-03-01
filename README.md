# host-port-enum

Simple yet fast host discovery tool plus port scanner, give input IP of current system, it discover all host for /16,/24 subnet mast as defined also it launch port scan against it withe specified range of port and also enumrate service running on open ports.

# Usage
```sh
PS M:\> python3 host-port-enum.py --help

██╗  ██╗ ██████╗ ███████╗████████╗   ██████╗  ██████╗ ██████╗ ████████╗   ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████║██║   ██║███████╗   ██║█████╗██████╔╝██║   ██║██████╔╝   ██║█████╗█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██╔══██║██║   ██║╚════██║   ██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝███████║   ██║      ██║     ╚██████╔╝██║  ██║   ██║      ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ By m4xx
usage: host-port-enum.py [-h] [-ip IP] [-p PORT] [-t THREAD]

optional arguments:
  -h, --help            show this help message and exit
  -ip IP, --ipAddress IP
                        Current System IP Address
  -p PORT, --port PORT  Port range
  -t THREAD, --thread THREAD
                        Threads Counts
```

# Output
```sh
PS M:\> python3 host-port-enum.py -ip 192.168.68.111 -p 1-65535 -t 200

██╗  ██╗ ██████╗ ███████╗████████╗   ██████╗  ██████╗ ██████╗ ████████╗   ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████║██║   ██║███████╗   ██║█████╗██████╔╝██║   ██║██████╔╝   ██║█████╗█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██╔══██║██║   ██║╚════██║   ██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝███████║   ██║      ██║     ╚██████╔╝██║  ██║   ██║      ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ By m4xx

==================================================

[!] Starting Host Discovery For:  192.168.68.0/16

==================================================

[+]  192.168.68.1  Host is alive on the network
[+]  192.168.68.111  Host is alive on the network
[+]  192.168.68.101  Host is alive on the network
[+]  192.168.68.103  Host is alive on the network
[+]  192.168.68.115  Host is alive on the network
[+]  192.168.68.113  Host is alive on the network
[+]  192.168.68.104  Host is alive on the network
[+]  192.168.68.112  Host is alive on the network
[+]  192.168.68.100  Host is alive on the network
[+]  192.168.68.106  Host is alive on the network


====================================================

[!]  Scanning Port for range 1-65535 on all live hosts

====================================================

Discovered port 7000 running bbs on 192.168.68.101 
Discovered port 53 running domain on 192.168.68.1 
Discovered port 7100 running font-service on 192.168.68.101 
Discovered port 6379 running redis on 192.168.68.106 
Discovered port 5432 running postgresql on 192.168.68.106 
```
