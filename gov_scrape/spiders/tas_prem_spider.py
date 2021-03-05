import scrapy
from scrapy_rss import RssItem


class TasPremSpider(scrapy.Spider):
    name = "tas_prem_spider"

    custom_settings = {
        "FEED_FILE": "./feeds/tas-prem.rss",
        "FEED_TITLE": "Premier of Tasmania",
        "FEED_LINK": "http://www.premier.tas.gov.au/media_release_search?queries_portfolio_query=Premier",
        "FEED_DESCRIPTION": "Media statements from the Premier of South Australia",
        "FEED_EXPORTER": "gov_scrape.exporters.TasGovRssItemExporter",
    }

    def start_requests(self):
        url = "http://www.premier.tas.gov.au/media_release_search?queries_portfolio_query=Premier"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css("h4.mr-topic a::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css('meta[property="og:title"]::attr(content)').get()
        item.link = response.url
        item.guid = response.url
        item.pubDate = response.css("h4::text").get().strip()
        item.author = response.css("div.header h1::text").get()
        item.description = "".join(response.css('div[style="width:100%"] p').getall())
        yield item
