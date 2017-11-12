# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EngNewsCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field() # 카테고리 ex) National, Business, Life&Style ..
    subcategory = scrapy.Field() # 서브 카테고리 ex) National - Politics, Social Affairs ..
    title = scrapy.Field() # 제목
    url = scrapy.Field() # 기사링크
    date = scrapy.Field() # 날짜
    article = scrapy.Field() #기사내용

    pass