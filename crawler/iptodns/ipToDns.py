import MySQLdb
import socket

class IpToDns:

    MIN_INT_IP = 16843009
    MAX_INT_IP = 4294967295
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

    def get_all_IPs(self):
        for int_ip in xrange(self.MIN_INT_IP, self.MAX_INT_IP):
            yield socket.inet_ntoa(hex(int_ip)[2:].zfill(8).decode('hex'))

    def get_hostname_by_IP(self, ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return False
