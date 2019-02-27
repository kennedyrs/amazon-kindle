# -*- coding: utf-8 -*-
import scrapy


class KindleTelegramSpider(scrapy.Spider):
    name = 'kindle_telegram'
    allowed_domains = ['https://www.amazon.com.br/']
    start_urls = ['https://www.amazon.com.br/gp/product/B0773XBMB6/']

    def parse(self, response):
        name = response.xpath('//span[@id="priceblock_ourprice"]/text()').get()
        self.log('O Preço do Kindle Papperwhite %s' % name)
