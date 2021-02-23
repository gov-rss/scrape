from scrapy_rss.exporters import RssItemExporter


class VicGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Victoria"
        )
        super().__init__(*args, **kwargs)


class NswGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of New South Wales"
        )
        super().__init__(*args, **kwargs)


class QldGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Queensland"
        )
        super().__init__(*args, **kwargs)


class WaGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Western Australia"
        )
        super().__init__(*args, **kwargs)