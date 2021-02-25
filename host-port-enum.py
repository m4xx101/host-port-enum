import os
import sys
from datetime import datetime
import socket
import threading

ports = {20:"FTP",21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",50:"IPSec",51:"IPSec",53:"DNS",67:"DHCP",68:"DHCP",69:"TFTP",80:"HTTP",110:"POP3",119:"NNTP",123:"NTP",135:"NetBIOS",136:"NetBIOS",137:"NetBIOS",138:"NetBIOS",139:"NetBIOS",143:"IMAP4",161:"SNMP",162:"SNMP",389:"LDAP",443:"HTTP-SSL",989:"SFTP",990:"SFTP",3389:"RDP",1433:"MSSQL",8080:"Jenkins",8081:"Jenkins"}

def pingit(x):
    cmd= "ping -n 1 " + x
    result=os.popen(cmd)
    for line in result.readlines():
        if(line.find("ttl") != -1):
            alive.append(x)
            print("[+] {} Host is alive on the network".format(x))

def scan(host,ports, service):
        socket.setdefaulttimeout(1)
        result=socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect_ex((host,ports))
        if result == 0:
            print("Discovered open port {} running {} on {} ".format(ports,service, host))
            socket.socket(socket.AF_INET,socket.SOCK_STREAM).close()

t1 = datetime.now()
IP = sys.argv[1]
tmp=IP.split('.')
newip=[]
alive=[]
net1=tmp[0]+'.'+tmp[1]+'.'+'0'+'.'+'0'
for ip in range(1,255):
    for ip2 in range(1,255):
        newip.append(tmp[0]+'.'+tmp[1]+'.'+str(ip)+'.'+str(ip2))

workref = []
print('='*50 + '\n')
print("Starting Scanning: For {}/24\n".format(net1))
print('='*50 + '\n')
for k in newip:
    workers = threading.Thread(target=pingit,args=(k,))
    workref.append(workers)
    workers.start()
for k in workref:
    k.join()
print('')
print('='*50 + '\n')
print('Port scanning in progress....\n')
print('='*50 + '\n')
getport=ports.keys()
threads=[]
for o in alive:
    for key in getport:
        t1 = threading.Thread(target=scan,args=(o,key, ports[key]))
        threads.append(t1)
        t1.start()

for thread in threads:
    thread.join()
