# -*- coding: utf-8 -*-
import json

import scrapy


class FshxtSpider(scrapy.Spider):
    name = 'fshxt'
    allowed_domains = ['m.fshxt.com']
    start_urls = ['http://m.fshxt.com/api.php?m=quotes&s=qh&list=CAD%2CAHD%2CZSD%2CNID%2CCU0%2CAL0%2CZN0%2CNI0%2CGC%2CSI']

    def parse(self, response):
        sites = json.loads(response.body_as_unicode())
        if sites.get('success') == True:
            d=[]
            for site in sites.get('rows'):
                for i in site:
                  d.append(i)
            print(d)
