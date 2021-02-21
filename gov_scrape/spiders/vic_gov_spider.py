import scrapy
from scrapy_splash import SplashRequest
from gov_scrape.items import RssFeedItem


class VicGovScrapeSpider(scrapy.Spider):
    name = "vic_gov_scrape"

    custom_settings = {
        "FEED_FILE": "./feeds/vic-gov.rss",
        "FEED_TITLE": "Media Centre | Premier of Victoria",
        "FEED_LINK": "https://www.premier.vic.gov.au/media-centre",
        "FEED_DESCRIPTION": "Posts from the Victorian State Government's media centre",
        "FEED_EXPORTER": "gov_scrape.exporters.VicGovRssItemExporter",
    }

    def start_requests(self):
        url = "https://www.premier.vic.gov.au/media-centre?page=%d"
        for i in range(1, 2):
            yield SplashRequest(url % i, self.parse, args={"wait": 0.5})

    def parse(self, response):
        post_links = response.css(
            "a.rpl-search-results__item::attr(data-print-url)"
        ).getall()
        for url in post_links:
            yield SplashRequest(url, self.parse_item, args={"wait": 0.5})

    def parse_item(self, response):
        date_pattern = (
            r'field_news_date:"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}"'
        )

        item = RssFeedItem()
        item.rss.title = response.css("title::text").get().split(" | ")[0]
        item.rss.link = response.url
        item.rss.guid = response.url
        item["pubDate"] = (
            response.css("script::text")
            .re_first(date_pattern)
            .split(":", maxsplit=1)[-1]
            .strip('"')
        )
        item.rss.description = "".join(response.css("div.rpl-markup__inner p").getall())
        item.rss.author = "State Government of Victoria"
        yield item
