import scrapy
from scrapy_rss import RssItem


class ActShadowSpider(scrapy.Spider):
    name = "act_shadow"

    custom_settings = {
        "FEED_FILE": "./feeds/act-liberals.rss",
        "FEED_TITLE": "Canberra Liberals",
        "FEED_LINK": "https://canberraliberals.org.au/news",
        "FEED_DESCRIPTION": "The lastest News, Media Releases and Speeches from the Canberra Liberals",
        "FEED_EXPORTER": "gov_scrape.exporters.ActShadowRssItemExporter",
    }

    def start_requests(self):
        url = "https://canberraliberals.org.au/news"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css(
            ".articles-full-page-feed .content-main h3 a::attr(href)"
        ).getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css('meta[property="og:title"]::attr(content)').get()
        item.author = " & ".join(response.css(".contributor .name::text").getall())
        item.pubDate = response.css(
            'meta[property="article:published_time"]::attr(content)'
        ).get()
        item.link = response.url
        item.guid = response.url
        item.description = response.css(".content").get()
        yield item
