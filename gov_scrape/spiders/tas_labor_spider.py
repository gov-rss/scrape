import re
import scrapy
from scrapy_rss import RssItem


class TasLaborSpider(scrapy.Spider):
    name = "tas_labor"

    custom_settings = {
        "FEED_FILE": "./feeds/tas-labor.rss",
        "FEED_TITLE": "Tasmanian Labor",
        "FEED_LINK": "https://taslabor.com/news/",
        "FEED_DESCRIPTION": "News and media releases from Tasmanian Labor",
        "FEED_EXPORTER": "gov_scrape.exporters.TasShadowRssItemExporter",
    }

    def start_requests(self):
        url = "https://taslabor.com/news/"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css("article a::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css("title::text").get().rsplit(" - ", 1)[0]
        item.author = "Tasmanian Labor"
        item.link = response.url
        item.guid = response.url
        item.pubDate = response.css(
            'meta[property="article:published_time"]::attr(content)'
        ).get()
        description = response.css(".content-body").get()
        description = re.sub(r"<h2>.*?</h2>.*<time>.*?</time>", "", description)
        item.description = description
        yield item