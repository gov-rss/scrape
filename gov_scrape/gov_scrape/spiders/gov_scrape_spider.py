import scrapy
from scrapy_splash import SplashRequest


class GovScrapeSpider(scrapy.Spider):
    name = 'gov_scrape'

    def start_requests(self):
        url = "https://www.premier.vic.gov.au/media-centre?page=%d"
        for i in range(1, 2):
            yield SplashRequest(url % i, self.parse, args={'wait': 0.5})

    def parse(self, response):
        post_links = response.css('a.rpl-search-results__item::attr(data-print-url)').getall()
        for url in post_links:
            yield SplashRequest(url, self.parse_post, args={'wait': 0.5})

    def parse_post(self, response):
        date_pattern = r'field_news_date:"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}"'
        yield {
            'title': response.css('title::text').get().split(' | ')[0],
            'link': response.url,
            'creator': "Victorian State Government",
            'pubDate':  response.css('script::text').re_first(date_pattern).split(':', maxsplit=1)[-1].strip('"'),
            'description': response.css('meta[name=description]::attr(content)').get(),
            'content': ''.join(response.css('div.rpl-markup__inner p').getall()),
        }
