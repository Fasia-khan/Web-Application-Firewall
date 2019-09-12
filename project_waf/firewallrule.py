import os
import iptablexe as ipt
#import findusername
def firewallrulestart():
    usrname='root'
    check = True
    while check:
        try:
            exists = os.path.isfile('/%s/Desktop/project_waf/ipsumclone/ipsum/ipsum.txt'%(usrname))
            print(exists)
            count = 0
            if exists:
                gitfile = open("/%s/Desktop/project_waf/ipsumclone/ipsum/ipsum.txt"%(usrname), 'r')
                for ips in gitfile:
                    count = count + 1
                    if count < 5:
                        continue
                    iplvl = ips.split()
                    if int(iplvl[1]) >= 4:
                        ipt.iptable_module(iplvl[0])  # src values from ipsum file  to iptablexe.py
                        # send ip to iptable rule execution modules
                        print(count, ':', iplvl)

        except IOError:
            os.chdir("/%s/Desktop/project_waf/ipsumclone/"%(usrname))
            print(os.listdir())
            os.system("git clone https://github.com/stamparm/ipsum.git")
        check = False
