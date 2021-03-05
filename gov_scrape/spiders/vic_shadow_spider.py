import scrapy
from ..items import RssFeedItem


class VicShadowSpider(scrapy.Spider):
    name = "vic_shadow_spider"

    custom_settings = {
        "FEED_FILE": "./feeds/vic-shadow.rss",
        "FEED_TITLE": "Media Releases | Liberal Victoria",
        "FEED_LINK": "https://vic.liberal.org.au/MediaReleases/",
        "FEED_DESCRIPTION": "Media releases from Liberal Victoria",
        "FEED_EXPORTER": "gov_scrape.exporters.VicShadowRssItemExporter",
    }

    def start_requests(self):
        url = "https://vic.liberal.org.au/MediaReleases/"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css("a.button.outline::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssFeedItem()
        item.rss.title = response.css('meta[property="og:title"]::attr(content)').get()
        item.rss.link = response.url
        item.rss.guid = response.url
        item["pubDate"] = response.css(".title h6::text").get()
        item.rss.author = "Liberal Victoria"
        item.rss.description = "".join(response.css(".mr-content").extract())
        yield item