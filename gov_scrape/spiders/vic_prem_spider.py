import base64
import scrapy
from scrapy_splash import SplashRequest
from scrapy_rss import RssItem


class VicPremSpider(scrapy.Spider):
    name = "vic_prem"

    custom_settings = {
        "FEED_FILE": "./feeds/vic-prem.rss",
        "FEED_TITLE": "Premier of Victoria",
        "FEED_LINK": "https://www.premier.vic.gov.au/media-centre",
        "FEED_DESCRIPTION": "Posts from the Victorian State Government's media centre",
        "FEED_EXPORTER": "gov_scrape.exporters.VicGovRssItemExporter",
    }

    def start_requests(self):
        # for some reason calling SplashRequest with a lua script works
        # but a standard call using SplashRequest(url, self.parse, args={'wait': 10}) does not
        script = """
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(10))
            return {
                html = splash:html(),
            }
        end
        """

        url = "https://www.premier.vic.gov.au/media-centre?page=%d"
        for i in range(1, 3):
            yield SplashRequest(
                url % i, self.parse, endpoint="execute", args={"lua_source": script}
            )

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

        item = RssItem()
        item.title = response.css("title::text").get().split(" | ")[0]
        item.link = response.url
        item.guid = response.url
        item.pubDate = (
            response.css("script::text")
            .re_first(date_pattern)
            .split(":", maxsplit=1)[-1]
            .strip('"')
        )
        item.description = "".join(response.css("div.rpl-markup__inner p").getall())
        item.author = "State Government of Victoria"
        yield item
