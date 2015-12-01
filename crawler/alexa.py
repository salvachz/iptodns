#!/usr/local/bin/python2.7

import scrapy
import socket
import MySQLdb


class BlogSpider(scrapy.Spider):
    name = 'Alexa'
    start_urls = ['http://www.alexa.com/topsites/']
    querys = {
        'insertDNS': """INSERT IGNORE INTO Dns (dnsId, dnsName) VALUES (NULL, '%s')""",
        'getDnsId': """SELECT dnsId FROM Dns WHERE dnsName = '%s'""",
        'insertIP': """INSERT IGNORE INTO DnsIp (dipDnsId, dipIp) VALUES (%s, INET_ATON('%s'))""",
    }
    

    def parse(self, response):
        url = 'http://www.alexa.com/topsites/global;%s'
        for x in range(20):
            yield scrapy.Request(response.urljoin(url % x), self.parse_pages)

    def parse_pages(self, response):
        mysql_con = MySQLdb.connect(host='127.0.0.1', user='root',
                                         passwd='', port=3306)
        mysql_con.select_db('iptodns')
        mysql = mysql_con.cursor()
        for url in response.css('#alx-content > div > section.content-fixed.page-product-content > span > span > section > div.listings > ul > li > div.desc-container > p > a::text').extract():
            domain = url.lower()
            ips = socket.gethostbyname_ex('%s' % domain)[2]
            mysql.execute(self.querys['insertDNS'] % domain)
            mysql.execute(self.querys['getDnsId'] % domain)
            row = mysql.fetchone()
            dns_id = row[0]
            for ip in ips:
                mysql.execute(self.querys['insertIP'] % (dns_id,ip))
            yield {'domain': domain, 'IPs':ips}
