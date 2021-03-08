from scrapy_rss.exporters import RssItemExporter


class ActShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get("copyright", "Copyright Canberra Liberals")
        super().__init__(*args, **kwargs)


class NswGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of New South Wales"
        )
        super().__init__(*args, **kwargs)


class NtShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get("copyright", "Copyright Country Liberal Party")
        super().__init__(*args, **kwargs)


class SaGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of South Australia"
        )
        super().__init__(*args, **kwargs)


class QldGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Queensland"
        )
        super().__init__(*args, **kwargs)


class QldShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright Liberal National Party"
        )
        super().__init__(*args, **kwargs)


class SaShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get("copyright", "Copyright Labor South Australia")
        super().__init__(*args, **kwargs)


class TasGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Tasmania"
        )
        super().__init__(*args, **kwargs)


class TasShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get("copyright", "Copyright Tasmanian Labor")
        super().__init__(*args, **kwargs)


class VicGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Victoria"
        )
        super().__init__(*args, **kwargs)


class VicShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get("copyright", "Copyright Liberal Victoria")
        super().__init__(*args, **kwargs)


class WaGovRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get(
            "copyright", "Copyright State Government of Western Australia"
        )
        super().__init__(*args, **kwargs)


class WaShadowRssItemExporter(RssItemExporter):
    def __init__(self, *args, **kwargs):
        kwargs["language"] = kwargs.get("language", "en-AU")
        kwargs["copyright"] = kwargs.get("copyright", "Liberal Party Western Australia")
        super().__init__(*args, **kwargs)