#!/usr/local/bin/python2.7

from iptodns import IpToDns

ipToDns = IpToDns()
print 'ha'
for ip in ipToDns.get_all_IPs():
    print ip
    raw_input()
