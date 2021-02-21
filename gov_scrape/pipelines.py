# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import dateparser
from scrapy_rss import RssedItem


class GovScrapePipeline:
    def process_item(self, item, spider):
        if isinstance(item, RssedItem):
            item.rss.pubDate = dateparser.parse(
                item["pubDate"], settings={"RETURN_AS_TIMEZONE_AWARE": True}
            )
        return item
