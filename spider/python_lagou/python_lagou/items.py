# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythonLagouItem(scrapy.Item):
    # define the fields for your item here like:
    companyFullName = scrapy.Field()
    companyLabelList = scrapy.Field()
    companyShortName = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    formatCreateTime = scrapy.Field()
    imState = scrapy.Field()
    industryField = scrapy.Field()
    positionAdvantage = scrapy.Field()
    positionLables = scrapy.Field()
    positionName = scrapy.Field()
    salary = scrapy.Field()
    thirdType = scrapy.Field()
    workYear = scrapy.Field()
