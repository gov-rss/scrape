# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_rss import RssedItem


class RssFeedItem(RssedItem):
    title = scrapy.Field()
    link = scrapy.Field()
    create = scrapy.Field()
    pubDate = scrapy.Field()
    description = scrapy.Field()
