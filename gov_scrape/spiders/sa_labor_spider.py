import scrapy
from scrapy_splash import SplashRequest
from scrapy_rss import RssItem


class SaLaborSpider(scrapy.Spider):
    name = "sa_labor"

    custom_settings = {
        "FEED_FILE": "./feeds/sa-labor.rss",
        "FEED_TITLE": "South Australian Labor",
        "FEED_LINK": "https://www.facebook.com/SouthAustralianLabor/",
        "FEED_DESCRIPTION": "Posts from South Australian Labor's Facebook feed",
        "FEED_EXPORTER": "gov_scrape.exporters.SaShadowRssItemExporter",
    }

    script = """
        function main(splash, args)
            splash:set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0")
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    """

    def start_requests(self):
        url = "https://www.facebook.com/SouthAustralianLabor/posts"
        yield SplashRequest(
            url, self.parse, endpoint="execute", args={"lua_source": self.script}
        )

    def parse(self, response):
        post_links = response.css(
            'span a[href^="https://www.facebook.com/SouthAustralianLabor/posts/"]::attr(href)'
        ).getall()
        yield from [
            SplashRequest(
                post_url,
                self.parse_item,
                endpoint="execute",
                args={"lua_source": self.script},
            )
            for post_url in post_links
        ]

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css(
            'meta[property="og:description"]::attr(content)'
        ).get()
        item.author = "South Australian Labor"
        item.link = response.url
        item.guid = response.url
        item.pubDate = response.css(".timestampContent").get()
        item.description = "".join(
            response.css('div[data-testid="post_message"]').getall()
        )
        yield item
