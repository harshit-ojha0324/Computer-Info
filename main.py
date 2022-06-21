# import module
import subprocess
data = subprocess.check_output(['ipconfig', '/all']).decode('utf-8')
count=0
count2=0
t=0
s=data.split('\r\n\r\n')
for item in s:
    count+=1
    if(item=="Wireless LAN adapter Wi-Fi:"):

        t=count+1
    if(t==count):
        u=item.split('\r\n')
        for item in u:

            count2+=1
            if("Link-local IPv6 Address" in item):
                print(item)
            if(count2==7):
                print(item)
            if(count2==8):
                print(item)
            if(count2==11):
                print(item)




print(f"Number of adapters are: {count}")

