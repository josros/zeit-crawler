# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZeitArticleItem(scrapy.Item):
    link = scrapy.Field()
    kicker = scrapy.Field()
    dates = scrapy.Field()
    header = scrapy.Field()
    summary = scrapy.Field()
    body = scrapy.Field()
    subheaders = scrapy.Field()
    tags = scrapy.Field()
