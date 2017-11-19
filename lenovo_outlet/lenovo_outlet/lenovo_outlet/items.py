# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LenovoOutletItem(scrapy.Item):
    department = scrapy.Field()
    title = scrapy.Field()
    in_stock = scrapy.Field()
    email = scrapy.Field()
