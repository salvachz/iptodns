#!/usr/local/bin/python2.7

import scrapy
from iptodns import IpToDns


class BlogSpider(scrapy.Spider):
    name = 'Alexa'
    start_urls = ['http://www.alexa.com/topsites/']
    

    def parse(self, response):
        url = 'http://www.alexa.com/topsites/global;%s'
        for x in range(20):
            yield scrapy.Request(response.urljoin(url % x), self.parse_pages)

    def parse_pages(self, response):
        ipToDns = IpToDns()
        for url in response.css('#alx-content > div > section.content-fixed.page-product-content > span > span > section > div.listings > ul > li > div.desc-container > p > a::text').extract():
            domain = url.lower()
            dns_id = ipToDns.add_DNS(domain)
            ips = ipToDns.get_IPs(domain)
            for ip in ips:
                ipToDns.add_IP_to_DNS(ip, dns_id)
            yield {'domain': domain, 'IPs':ips}
