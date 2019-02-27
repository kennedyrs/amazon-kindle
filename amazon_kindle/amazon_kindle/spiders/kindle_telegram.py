# -*- coding: utf-8 -*-
import scrapy


class KindleTelegramSpider(scrapy.Spider):
    name = 'kindle_telegram'
    allowed_domains = ['https://www.amazon.com.br/']
    start_urls = ['http://https://www.amazon.com.br//']

    def parse(self, response):
        pass
