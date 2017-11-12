# -*- coding: utf-8 -*-
 
import scrapy
import time
import csv
import json
from eng_news_crawler.items import EngNewsCrawlerItem

# 기사 url 크롤링 
class NewsUrlSpider(scrapy.Spider):
	name = "newsUrlCrawler"

	def start_requests(self):
		# National, Business, Life&Style, Entertainment, Sports, World
		# category = ['020100000000', '020200000000', '020300000000', '020400000000', '020500000000', '021200000000']
		category = ['020100000000']

		for ct in category:
			# for i in range(1, 11):
			for i in range(1, 2):
				yield scrapy.Request("http://www.koreaherald.com/list.php?ct={0}&ctv=0&np={1}".format(ct, i), callback=self.parse_news)

	def parse_news(self, response):

		for sel in response.xpath('body/div/div[3]/div[2]/div/ul[1]'):
			item = EngNewsCrawlerItem()

			# item['subcategory'] = sel.xpath('//li/div[3]/a/text()').extract()
			# item['title'] = sel.xpath('//li/div[2]/p[1]/a/text()').extract()
			item['url'] = sel.xpath('//li/div[2]/p[1]/a/@href').extract()
			# item['date'] = sel.xpath('//li/div[3]/p/text()').extract()

			yield item

# 기사 내용 크롤링
class NewsSpider(scrapy.Spider):
    name = "newsCrawler"
 
    def start_requests(self):

    	with open('news_list.json') as data_file:    
    		data = json.load(data_file)
    		for d in data:
    			for url in d["url"]:
    				yield scrapy.Request("http://www.koreaherald.com" + url, callback=self.parse_news)
 
    def parse_news(self, response):
        item = EngNewsCrawlerItem()

        item['category'] = response.xpath('body/div[1]/div[3]/div[2]/div/div[1]/p/text()').extract()[0]
        # item['subcategory'] = sel.xpath('//li/div[3]/a/text()').extract()

        item['title'] = response.xpath('body/div[1]/div[3]/div[2]/div/div[1]/div[3]/p/text()').extract()[0]
        item['article'] = response.xpath('//*[@id="articleText"]/text()').extract()

        item['date'] = response.xpath('body/div[1]/div[3]/div[2]/div/div[1]/div[3]/ul/li[1]/text()').extract()[0]
 
        yield item