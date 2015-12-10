#!/usr/local/bin/python2.7

from iptodns import IpToDns
import sys

if len(sys.argv) == 2:

    domain = sys.argv[1]
    ipToDns = IpToDns()
    dns_id = ipToDns.add_DNS(domain)
    ips = ipToDns.get_IPs(domain)
    for ip in ips:
        ipToDns.add_IP_to_DNS(ip, dns_id)
    print "OK! Add with success!"
else:
    print "Error"
