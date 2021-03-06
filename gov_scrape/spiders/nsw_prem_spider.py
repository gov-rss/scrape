import scrapy
from scrapy_rss.items import RssItem


class NswPremSpider(scrapy.Spider):
    name = "nsw_prem"

    custom_settings = {
        "FEED_FILE": "./feeds/nsw-prem.rss",
        "FEED_TITLE": "Ministers of New South Wales",
        "FEED_LINK": "https://www.nsw.gov.au/media-releases",
        "FEED_DESCRIPTION": "Posts from the New South Wales State Government's media centre",
        "FEED_EXPORTER": "gov_scrape.exporters.NswGovRssItemExporter",
    }

    def start_requests(self):
        url = "https://www.nsw.gov.au/media-releases"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css("h2.nsw-card__title a::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)
        next_page = (
            response.url
            + response.css('a[title="Show more results"]::attr(href)').get()
        )
        if next_page.endswith("page=1"):
            yield scrapy.Request(next_page, self.parse)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css("title::text").get().split(" | ")[0]
        item.link = response.url
        item.guid = response.url
        item.pubDate = response.css('meta[name="dcterms.date"]::attr(content)').get()
        item.description = response.css("div.nsw-wysiwyg-content").get()
        author = response.css("div.standard-header__released_by div::text").getall()
        if author:
            item.author = author[-1].strip()
        else:
            item.author = "NSW Government"

        yield item
