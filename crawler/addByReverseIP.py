#!/usr/local/bin/python2.7

from iptodns import IpToDns
from time import sleep

ipToDns = IpToDns()
print ipToDns.get_hostname_by_IP('74.86.144.194')
for ip in ipToDns.get_all_IPs():
    print ip,'->',ipToDns.get_hostname_by_IP(ip)
    sleep(0.1)
