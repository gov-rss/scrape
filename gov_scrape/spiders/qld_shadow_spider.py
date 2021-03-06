import scrapy
from scrapy_splash import SplashRequest
from scrapy_rss import RssItem


class QldShadowSpider(scrapy.Spider):
    name = "qld_shadow"

    custom_settings = {
        "FEED_FILE": "./feeds/qld-shadow.rss",
        "FEED_TITLE": "Liberal National Party Queensland",
        "FEED_LINK": "https://www.lnp.org.au/news/",
        "FEED_DESCRIPTION": "Facebook feed of the Queensland Liberal National Party",
        "FEED_EXPORTER": "gov_scrape.exporters.QldShadowRssItemExporter",
    }

    def start_requests(self):
        # clicks on the "see more" links in each post to reveal all text
        script = """
        function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(4))
            splash:set_viewport_full()
            splash:runjs([[
                var seeMoreElements = document.getElementsByClassName('cff-expand');
                for (var i = 0; i < seeMoreElements.length; i++) {
                    var link = seeMoreElements[i].children[0];
                    link.click();
                }
            ]])
            return splash:html()
        end
        """
        url = "https://www.lnp.org.au/news/"
        yield SplashRequest(
            url, self.parse, endpoint="execute", args={"lua_source": script}
        )

    def parse(self, response):
        post_elements = response.css(".cff-item.author-lnp---liberal-national-party")
        for post in post_elements:
            isVideoPost = True if post.css(".cff-video-post") else False
            item = RssItem()
            item.author = post.css("div.cff-page-name a::text").get()
            item.pubDate = post.css(".cff-date::text").get().strip()
            item.link = post.css(".cff-viewpost-facebook::attr(href)").get()
            item.guid = item.link.link
            if isVideoPost:
                item.title = post.css(".cff-poster::attr(alt)").get()
                item.description = post
            else:
                item.title = post.css(".cff-post-desc::text").get()
                item.description = post.css(".cff-post-desc").get()
            yield item
