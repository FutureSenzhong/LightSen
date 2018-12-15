# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy




class U17Item(scrapy.Item):
    # define the fields for your item here like:
    comic_id = scrapy.Field()
    title = scrapy.Field()
    cover = scrapy.Field()
    classfy = scrapy.Field()



