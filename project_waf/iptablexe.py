import os
#this is the function for ipsum -ip block
def iptable_module(src):
    s=src
    d='172.20.10.3'#ip should be changed every
    ipexe = 'sudo iptables -A INPUT -m tcp -p tcp -s '+s+' -d '+d+' --dport 80 -j DROP'#block the ips from file ipsum
    os.system(ipexe)
#this function for illegal use of sql key words
def iptable_adminblock(src):
    src_ip = src
    dst_ip = '172.20.10.3'  # ip should be changed every
    nat_dst_ip='172.20.10.4'
    ipexe = 'sudo iptables -A INPUT -m tcp -p tcp -s %s -d %s --dport 80 -j DROP'%(src_ip,dst_ip)#block the new ips from
    ipnat = 'sudo iptables -t nat -A PREROUTING -m tcp -p tcp -s %s -d %s -j DNAT --to-destination %s'%(src,dst_ip,nat_dst_ip)
    # route to different port hosting one default website
    os.system(ipexe)
    os.system(ipnat)


