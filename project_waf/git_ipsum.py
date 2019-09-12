import os
#import time
#import findusername
usrname='root'
os.chdir("/%s/Desktop/project_waf/ipsumclone"%(usrname))
var = os.listdir("/%s/Desktop/project_waf/ipsumclone"%(usrname))
print(var)
if 'ipsum1' in var:
    os.system('rm -rf ipsum1')
    var = os.listdir("/%s/Desktop/project_waf/ipsumclone"%(usrname))
if 'ipsum' in var:
    os.system('mv ipsum ipsum1')
    var = os.listdir("/%s/Desktop/project_waf/ipsumclone"%(usrname))
if 'ipsum' not in var:
    os.system('git clone https://github.com/stamparm/ipsum.git')
else:
    var = []
print(os.listdir("/%s/Desktop/project_waf/ipsumclone"%(usrname)))
# gitfile=open('/home/root/Desktop/project_waf/ipsumclone/ipsum/ipsum.txt')

# time.sleep(24*60*60)


