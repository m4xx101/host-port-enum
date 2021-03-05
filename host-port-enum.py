from ast import parse
import os
from os.path import split
import platform
import socket
import threading
import numpy as np
import argparse


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
hostip=get_ip_address()
protocolname = 'tcp'
newip=[]
print('''
██╗  ██╗ ██████╗ ███████╗████████╗   ██████╗  ██████╗ ██████╗ ████████╗   ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██║  ██║██╔═══██╗██╔════╝╚══██╔══╝   ██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝   ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████║██║   ██║███████╗   ██║█████╗██████╔╝██║   ██║██████╔╝   ██║█████╗█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
██╔══██║██║   ██║╚════██║   ██║╚════╝██╔═══╝ ██║   ██║██╔══██╗   ██║╚════╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
██║  ██║╚██████╔╝███████║   ██║      ██║     ╚██████╔╝██║  ██║   ██║      ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝      ╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ By m4xx''')

def arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('-ip','--ipAddress', dest = "IP", help='Current System IP Address')
        parser.add_argument('-p','--port',dest = "PORT", help='Port range', default="1-2000")
        parser.add_argument('-r','--range',dest = "range", help="Scanning range Example: /16,/24 ", default="/24")
        parser.add_argument('-t','--thread',dest = "thread", help='Threads Counts', default=57)
        args = parser.parse_args()
        return args

args = arguments()
tmp=args.IP.split('.')
oper = platform.system()
if (oper == "Windows"):
   ping1 = "ping -n 1 "
elif (oper == "Linux"):
   ping1 = "ping -c 1 "
else :
   ping1 = "ping -c 1 "

if args.range == "/16":
    net1=tmp[0]+'.'+tmp[1]+'.'+'0'+'.'+'0'+"/16"
    for ip in range(1,255):
        for ip2 in range(1,255):
            newip.append(tmp[0]+'.'+tmp[1]+'.'+str(ip)+'.'+str(ip2))
elif args.range == "/24":
    net1=tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+'0'+"/24"
    for ip in range(1,255):
        newip.append(tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+str(ip))
else:
    print("Invalid argument for --range,-r\n Try: -r /24")

def pingit(x):
    for k in x:
        cmd= ping1 + k
        result=os.popen(cmd)
        for line in result.readlines():
            if(line.find("ttl") != -1):
                alive.append(k)
                print("\033[93m[+]\033[0m \033[92m \033[1m{} \033[0m Host is alive on the network".format(k))

def scan(host,ports):
    for k in ports:
        result=socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect_ex((host,k))
        try:
            if result == 0:
                print ("\033[94mDiscovered\033[0m port\033[1m\033[93m %s\033[0m running\033[91m\033[1m %s\033[0m on\033[92m\033[1m %s\033[0m " %(k, socket.getservbyport(k, protocolname),host))
                socket.socket(socket.AF_INET,socket.SOCK_STREAM).close()
        except:
            pass
IP = args.IP
alive=[]
workref = []

print('\n'+'='*50 + '\n')
print("\033[93m\033[1m[!]\033[0m \033[91mStarting Host Discovery For: \033[0m\033[1m\033[94m{}\033[0m\n".format(net1))
print('='*50 + '\n')
split_ip=np.array_split(newip, int(args.thread))
for k in split_ip:
    workers = threading.Thread(target=pingit,args=(k,))
    workref.append(workers)
    workers.start()
for k in workref:
    k.join()

print('')
print('\n'+'='*52 + '\n')
print('\033[93m\033[1m[!]\033[0m \033[91m Scanning Port for range \033[0m\033[1m\033[94m{}\033[0m \033[91mon all live hosts\n\033[0m'.format(args.PORT))
print('='*52 + '\n')
getport=args.PORT.split('-')
allports=range(int(getport[0]),int(getport[1])+1)
threads=[]
split_port=np.array_split(allports, int(args.thread))
for o in alive:
    for prt in split_port:
        t1 = threading.Thread(target=scan,args=(o,prt))
        threads.append(t1)
        t1.start()

for thread in threads:
    thread.join()
