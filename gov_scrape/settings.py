import os

BOT_NAME = "gov_scrape"

SPIDER_MODULES = ["gov_scrape.spiders"]
NEWSPIDER_MODULE = "gov_scrape.spiders"

# Splash config
SPLASH_URL = f"http://{os.getenv('SPLASH_IP', 'localhost:8050')}"
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"

# Crawl responsibly
USER_AGENT = "gov_scrape (+https://gov-rss.github.io)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy
CONCURRENT_REQUESTS = 16

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "scrapy_splash.SplashDeduplicateArgsMiddleware": 100,
}

# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware": 500,
    "scrapy_splash.SplashCookiesMiddleware": 723,
    "scrapy_splash.SplashMiddleware": 725,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": 810,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "gov_scrape.pipelines.GovScrapePipeline": 500,
    "scrapy_rss.pipelines.RssExportPipeline": 950,
}

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
HTTPCACHE_STORAGE = "scrapy_splash.SplashAwareFSCacheStorage"
HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"
HTTPCACHE_GZIP = False
