import scrapy
from .nsw_prem_spider import NswPremSpider


class NswGovSpider(NswPremSpider):
    name = "nsw_gov_spider"

    custom_settings = {
        "FEED_FILE": "./feeds/nsw-gov.rss",
        "FEED_TITLE": "News | NSW Government",
        "FEED_LINK": "https://www.nsw.gov.au/news",
        "FEED_DESCRIPTION": "Posts from the New South Wales State Government's news centre",
        "FEED_EXPORTER": "gov_scrape.exporters.NswGovRssItemExporter",
    }

    def start_requests(self):
        url = "https://www.nsw.gov.au/news"
        yield scrapy.Request(url, self.parse)
