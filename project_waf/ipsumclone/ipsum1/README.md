![Logo](https://i.imgur.com/PyKLAe7.png)

[![License](https://img.shields.io/badge/license-Public_domain-red.svg)](https://wiki.creativecommons.org/wiki/Public_domain)

About
----

**IPsum** is a threat intelligence feed based on 30+ different publicly available [lists](https://github.com/stamparm/maltrail) of suspicious and/or malicious IP addresses. All lists are automatically retrieved and parsed on a daily (24h) basis and the final result is pushed to this repository. List is made of IP addresses together with a total number of (black)list occurrence (for each). Greater the number, lesser the chance of false positive detection and/or dropping in (inbound) monitored traffic. Also, list is sorted from most (problematic) to least occurent IP addresses.

As an example, to get a fresh and ready-to-deploy auto-ban list of "bad IPs" that appear on at least 3 (black)lists you can run:

```
curl --compressed https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt 2>/dev/null | grep -v "#" | grep -v -E "\s[1-2]$" | cut -f 1
```

If you want to try it with `ipset`, you can do the following:

```
sudo su
apt-get -qq install iptables ipset
ipset -q flush ipsum
ipset -q create ipsum hash:net
for ip in $(curl --compressed https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt 2>/dev/null | grep -v "#" | grep -v -E "\s[1-2]$" | cut -f 1); do ipset add ipsum $ip; done
iptables -I INPUT -m set --match-set ipsum src -j DROP
```

In directory [levels](levels) you can find preprocessed raw IP lists based on number of blacklist occurrences (e.g. [levels/3.txt](levels/3.txt) holds IP addresses that can be found on 3 or more blacklists).

**Important:** If you are planning to use `git` to get the content of this repository do it like `git clone --depth 1 https://github.com/stamparm/ipsum.git`

Wall of shame (2019-04-15)
----

|IP|DNS lookup|Number of (black)lists|
|---|---|--:|
171.25.193.25|tor-exit5-readme.dfri.se|11
171.25.193.20|tor-exit0-readme.dfri.se|11
178.73.215.171|178-73-215-171-static.glesys.net|10
197.231.221.211|exit1.ipredator.se|10
128.31.0.13|tor-exit.csail.mit.edu|9
89.234.157.254|marylou.nos-oignons.net|9
206.189.217.240|-|9
171.25.193.77|tor-exit1-readme.dfri.se|9
171.25.193.78|tor-exit4-readme.dfri.se|9
171.25.193.235|tor-exit3-readme.dfri.se|9
65.19.167.131|-|9
58.42.228.170|-|9
64.113.32.29|tor.t-3.net|9
31.220.40.54|exit4.tor-network.net|9
109.97.49.130|-|8
51.15.53.83|83-53-15-51.rev.cloud.scaleway.com|8
65.19.167.132|-|8
51.15.187.209|atomator.salazzo.net|8
185.104.120.60|exit06.brasshorncomms.uk|8
176.31.208.193|tor-exit1.netnik.xyz|8
185.220.101.5|-|8
185.220.101.3|-|8
202.150.142.38|host38.subnet142.comnet.net.id|8
185.220.101.44|-|8
185.220.101.46|-|8
192.160.102.170|ogopogo.relay.coldhak.com|8
198.96.155.3|exit.tor.uwaterloo.ca|8
192.42.116.16|tor-exit.hartvoorinternetvrijheid.nl|8
109.201.133.100||8
166.70.207.2|this.is.a.tor.node.xmission.com|8
163.172.160.182|182-160-172-163.rev.cloud.scaleway.com|8
185.220.102.8|-|8
18.85.192.253|wholesomeserver.media.mit.edu|8
193.32.163.89|-|8
77.247.181.162|chomsky.torservers.net|8
77.247.181.163|lumumba.torservers.net|8
115.238.245.2|-|8
176.10.104.240|tor1e1.digitale-gesellschaft.ch|8
54.36.222.37|ip37.ip-54-36-222.eu|8
186.227.231.244|-|8
45.67.14.60|-|8
42.61.24.202|-|8
185.254.120.6|-|8
77.247.181.165|politkovskaja.torservers.net|8
121.147.22.123|-|8
111.53.76.186|-|8
171.217.70.156|-|8
192.160.102.168|prawksi.relay.coldhak.com|8
205.185.114.232|mx32.songlige.com|8
217.170.197.89|nortor3.nortor.no|8
89.197.161.164|89-197-161-164.virtual1.co.uk|8
205.185.117.100|drinks.ladylearn.com|8
137.74.167.96|ns200.anycast.me.6290lv1irc.xyz|8
117.156.234.3|-|8
