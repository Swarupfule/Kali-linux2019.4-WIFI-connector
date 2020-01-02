import subprocess

import re
def ShowNetworks():
    result = subprocess.run(['iwlist', 'wlan0',"scan"], stdout=subprocess.PIPE)
    
    res=result.stdout.decode('utf-8')
    lis=re.split(r'[;,:\n\s]\s*', res)
    devs=[]
    res1=[]
    k=0
    for i in lis:
       
       if "ESSID" in i:
           devs.append(lis[k+1])
           #print(lis[k+1])
       k+=1

    for d in devs:
        res1.append(re.findall(r'"(.*?)"',d)[0])
    return res1


def connect(net):
    if net=="Swa":
        print("bn both equals")
    else:
        print("not ewqu",net,"Swa")
    result = subprocess.run(['iwconfig', 'wlan0',"essid",net], stdout=subprocess.PIPE)
    print(type(result))
  

def DHCPSetup():
    result = subprocess.run(['dhclient', '-v',"wlan0"], stdout=subprocess.PIPE)
    print(result)

one=ShowNetworks()
connect(one[0])
DHCPSetup()
