import scrapy
from scrapy_rss import RssItem


class WaShadowSpider(scrapy.Spider):
    name = "wa_shadow"

    custom_settings = {
        "FEED_FILE": "./feeds/wa-shadow.rss",
        "FEED_TITLE": "Liberal Party of Western Australia",
        "FEED_LINK": "https://www.waliberal.org.au/news/",
        "FEED_DESCRIPTION": "Media releases from the Liberal Party of Western Australia",
        "FEED_EXPORTER": "gov_scrape.exporters.WaShadowRssItemExporter",
    }

    def start_requests(self):
        url = "https://www.waliberal.org.au/news/"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css(".entry-featured-image-url::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)
        next_page = response.css('a.page[title="Page 2"]::attr(href)').get()
        if next_page:
            yield scrapy.Request(next_page, self.parse)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css("title::text").get()
        item.author = "Liberal Party of Western Australia"
        item.link = response.url
        item.guid = response.url
        item.pubDate = response.css(
            'meta[property="article:published_time"]::attr(content)'
        ).get()
        item.description = response.css(".entry-content").get()
        return item