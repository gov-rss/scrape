from scrapy_rss.exporters import RssItemExporter


class VicGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Victoria"
        )
        super(VicGovRssItemExporter, self).__init__(*args, **kwargs)
