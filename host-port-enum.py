import os
import sys
from datetime import datetime
import socket
import threading

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
protocolname = 'tcp' 
def pingit(x):
    cmd= "ping -n 1 " + x
    result=os.popen(cmd)
    for line in result.readlines():
        if(line.count("TTL")):
            alive.append(x)
            print("\033[93m[+]\033[0m \033[92m \033[1m{} \033[0m Host is alive on the network".format(x))

def scan(host,ports):
        socket.setdefaulttimeout(1)
        result=socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect_ex((host,ports))
        try:
            if result == 0:
                print ("\033[94mDiscovered\033[0m port\033[1m\033[93m %s\033[0m running\033[91m\033[1m %s\033[0m on\033[92m\033[1m %s\033[0m " %(ports, socket.getservbyport(ports, protocolname),host))
                socket.socket(socket.AF_INET,socket.SOCK_STREAM).close()
        except:
            pass
t1 = datetime.now()
IP = sys.argv[1]
tmp=IP.split('.')
newip=[]
alive=[]
net1=tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+'0'
for ip in range(1,255):
    newip.append(tmp[0]+'.'+tmp[1]+'.'+tmp[2]+'.'+str(ip))

workref = []
print('\n'+'='*50 + '\n')
print("\033[93m\033[1m[!]\033[0m \033[91mStarting Scanning: For\033[0m\033[1m\033[94m {}/16\033[0m\n".format(net1))
print('='*50 + '\n')
for k in newip:
    workers = threading.Thread(target=pingit,args=(k,))
    workref.append(workers)
    workers.start()
for k in workref:
    k.join()
print('')
print('\n'+'='*52 + '\n')
print('\033[93m\033[1m[!]\033[0m \033[91m Scanning Port for range {} on all live hosts\n\033[0m'.format(sys.argv[2]))
print('='*52 + '\n')
getport=sys.argv[2].split('-')
threads=[]
for o in alive:
    for prt in range(int(getport[0]),int(getport[1])):
        t1 = threading.Thread(target=scan,args=(o,prt))
        threads.append(t1)
        t1.start()

for thread in threads:
    thread.join()
