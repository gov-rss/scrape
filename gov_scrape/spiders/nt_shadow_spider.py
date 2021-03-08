import re
import scrapy
from scrapy_rss import RssItem


class NtShadowSpider(scrapy.Spider):
    name = "nt_shadow"

    custom_settings = {
        "FEED_FILE": "./feeds/nt-shadow.rss",
        "FEED_TITLE": "Country Liberal Party of the Northern Territory",
        "FEED_LINK": "http://www.countryliberal.org/",
        "FEED_DESCRIPTION": "Media releases from the Country Liberal Party of the Northern Territory",
        "FEED_EXPORTER": "gov_scrape.exporters.NtShadowRssItemExporter",
    }

    def start_requests(self):
        url = "http://www.countryliberal.org/"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        post_links = response.css(
            "div#nav li#wsite-nav-227609612986400502 div ul li a::attr(href)"
        ).getall()
        yield from response.follow_all(post_links, self.parse_item)

    def parse_item(self, response):
        item = RssItem()
        item.title = response.css('font[size="5"]::text').get()
        item.link = response.url
        item.guid = response.url
        item.author = " - ".join(response.css('font[size="6"]::text').getall()).strip()

        re_date = r"\d{1,2} [A-Z][a-z]+ \d{4}"
        item.pubDate = response.css(".paragraph").re_first(re_date)

        description = response.css("div.content-wrap .paragraph").get()
        description = re.sub(
            f"<strong>(<span .*?>)?<font .*?>{item.title.title}(<br>)?</font>(</span>)?</strong><br>",
            "",
            description,
        )
        description = re.sub(re_date + "<br><br>", "", description)
        item.description = description
        yield item
