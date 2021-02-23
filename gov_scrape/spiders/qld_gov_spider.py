from typing import AsyncIterable
import scrapy
from ..items import RssFeedItem


class QldGovSpider(scrapy.Spider):
    name = "qld_gov_spider"

    custom_settings = {
        "FEED_FILE": "./feeds/qld-gov.rss",
        "FEED_TITLE": "Media Statements | Queensland Government",
        "FEED_LINK": "https://statements.qld.gov.au/",
        "FEED_DESCRIPTION": "Media statements from the Queensland State Government",
        "FEED_EXPORTER": "gov_scrape.exporters.QldGovRssItemExporter",
    }

    def start_requests(self):
        url = "https://statements.qld.gov.au/?pageIndex=%d"
        for i in range(1, 3):
            yield scrapy.Request(url % i, self.parse)

    def parse(self, response):
        post_links = response.css("div.caption p a::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssFeedItem()
        item.rss.title = (
            response.css('meta[name="DCTERMS.title"]::attr(content)').get().strip()
        )
        item.rss.link = response.url
        item.rss.guid = response.url
        item["pubDate"] = (
            response.css("script::text")
            .re_first(r'"datePublished": ".*"')
            .split(":", 1)[-1]
            .strip(' "')
        )
        author = response.css("p.statement-ministers::text").getall()
        item.rss.author = " & ".join(author)
        description = response.css("div div p").getall()
        cutoff = 2  # publish date & author
        if len(author) > 1:
            cutoff += len(author)
        item.rss.description = "".join(description[cutoff:])
        yield item
