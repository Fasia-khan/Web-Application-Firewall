import os
import time
import firewallrule
#import findusername
usrname='root'
#dst_ip='192.168.0.108'
os.chdir("/%s/Desktop/project_waf/"%(usrname))
cmdgit = 'python git_ipsum.py'
cmdfinalcap3 = 'python finalcap3.py'
#first we clone the ipsum file
os.system(cmdgit)
time.sleep(10)
#then flush the previous rules of iptables
os.system('sudo iptables -F INPUT')
os.system("for i in $(sudo  iptables -t nat --line-numbers -L | grep ^[0-9] | awk '{ print $1 }' | tac ); do sudo iptables -t nat -D PREROUTING $i; done")
#os.system('sudo iptables -t nat -I PREROUTING --src 0/0 --dst %s -p tcp --dport 80 -j REDIRECT --to-ports 8888'%(dst_ip))
time.sleep(5)
#then add all the rules from ipsum file
firewallrule.firewallrulestart()
time.sleep(5)
#finally run packet sniffer
os.system(cmdfinalcap3)
while True:
    time.sleep(24*60*60)
    os.system(cmdgit)
