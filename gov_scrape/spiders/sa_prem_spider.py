import scrapy
from ..items import RssFeedItem


class SaPremSpider(scrapy.Spider):
    name = "sa_prem_spider"

    custom_settings = {
        "FEED_FILE": "./feeds/sa-prem.rss",
        "FEED_TITLE": "Media Releases | Premier of SA",
        "FEED_LINK": "https://www.premier.sa.gov.au/news/media-releases",
        "FEED_DESCRIPTION": "Media statements from the Premier of South Australia",
        "FEED_EXPORTER": "gov_scrape.exporters.SaGovRssItemExporter",
    }

    def start_requests(self):
        url = "https://www.premier.sa.gov.au/news/media-releases?collection=premier-push&form=media-releases&profile=_default_preview&sort=dmetad&start_rank=%d"
        for i in range(0, 2):
            yield scrapy.Request(url % (i * 12 + 1), self.parse)

    def parse(self, response):
        post_links = response.css("a.news-listing-grid__link::attr(href)").getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssFeedItem()
        item.rss.title = response.css('meta[name="dcterms.title"]::attr(content)').get()
        item.rss.link = response.url
        item.rss.guid = response.url

        item["pubDate"] = response.css(
            'meta[name="dcterms.issued"]::attr(content)'
        ).get()

        item.rss.author = response.css(
            'meta[name="article.minister"]::attr(content)'
        ).get()

        summary = response.css("div.news-detail__summary p").getall()
        body = response.css("div.news-detail__body p").getall()
        item.rss.description = "".join(summary + body)
        return item