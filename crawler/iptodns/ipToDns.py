import MySQLdb
import socket

class IpToDns:

    querys = {
        'insertDNS': """INSERT IGNORE INTO Dns (dnsId, dnsName) VALUES (NULL, '%s')""",
        'getDnsId': """SELECT dnsId FROM Dns WHERE dnsName = '%s'""",
        'insertIP': """INSERT IGNORE INTO DnsIp (dipDnsId, dipIp) VALUES (%s, INET_ATON('%s'))""",
    }

    def __init__(self):
        self.mysql_con = MySQLdb.connect(host='127.0.0.1', user='root',
                           passwd='', port=3306)
        self.mysql_con.select_db('iptodns')
        self.mysql = self.mysql_con.cursor()

    def add_DNS(self, domain):
        self.mysql.execute(self.querys['insertDNS'] % domain)
        self.mysql.execute(self.querys['getDnsId'] % domain)
        row = self.mysql.fetchone()
        return row[0]

    def add_IP_to_DNS(self, ip, dns_id):
        self.mysql.execute(self.querys['insertIP'] % (dns_id,ip))

    def get_IPs(self, domain):
        try:
            return socket.gethostbyname_ex('%s' % domain)[2]
        except:
            return []


