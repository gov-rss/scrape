import scrapy
from scrapy_rss.items import RssItem


class WaGovSpider(scrapy.Spider):
    name = "wa_gov_spider"

    custom_settings = {
        "FEED_FILE": "./feeds/wa-gov.rss",
        "FEED_TITLE": "Government of Western Australia",
        "FEED_LINK": "https://www.mediastatements.wa.gov.au",
        "FEED_DESCRIPTION": "Media statements from the Government of Western Australia",
        "FEED_EXPORTER": "gov_scrape.exporters.WaGovRssItemExporter",
    }

    def start_requests(self):
        url = "https://www.mediastatements.wa.gov.au/Pages/Default.aspx"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css("td a::attr(href)").getall()[:24]
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css("title::text").get().split(" - ", 1)[-1].strip()
        item.link = response.url
        item.guid = response.url
        item.pubDate = response.css("div.newsCreatedDate::text").get().strip()
        item.author = " & ".join(response.css("img.ministersPic::attr(alt)").getall())
        item.description = response.css("div.ms-rtestate-field").get()
        yield item
