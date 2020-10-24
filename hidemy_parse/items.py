# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HidemyParseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class proxy(scrapy.Item):
    protocol=scrapy.Field()
    ip = scrapy.Field()
    port = scrapy.Field()