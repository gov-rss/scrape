# gov-scrape

A collection of Scrapy spiders that transform government media releases to
RSS feeds. The purpose of creating these is to increase the availability of these media releases to members of the public, making it easier to keep up to date with the movements of state governments.

## Setup

### Pip

```shell
pip install -r requirements.txt
```

### Conda

```shell
conda create --file=environment.yaml
conda activate gov-scrape
```

## Run

```shell
scrapy crawl <spider-name>
```

### Available spiders

| Spider Name                                             | Source                                                                             |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [nsw_gov](./gov_scrape/spiders/nsw_gov_spider.py)       | https://www.nsw.gov.au/news                                                        |
| [nsw_prem](./gov_scrape/spiders/nsw_prem_spider.py)     | https://www.nsw.gov.au/media-releases                                              |
| [qld_gov](./gov_scrape/spiders/qld_gov_spider.py)       | https://statements.qld.gov.au/                                                     |
| [sa_prem](./gov_scrape/spiders/sa_prem_spider.py)       | https://www.premier.sa.gov.au/news/media-releases                                  |
| [tas_prem](./gov_scrape/spiders/tas_prem_spider.py)     | http://www.premier.tas.gov.au/media_release_search?queries_portfolio_query=Premier |
| [vic_prem](./gov_scrape/spiders/vic_prem_spider.py)     | https://www.premier.vic.gov.au/media-centre                                        |
| [vic_shadow](./gov_scrape/spiders/vic_shadow_spider.py) | https://vic.liberal.org.au/MediaReleases/                                          |
| [wa_gov](./gov_scrape/spiders/wa_gov_spider.py)         | https://www.mediastatements.wa.gov.au/Pages/Default.aspx                           |

A few sources already had RSS feeds available, a list of these is available below:

| RSS Feed                                                                                                                                             | Source                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [Jodie McKay Media Releases (NSW Shadow Premier)](https://www.jodimckay.com.au/media_releases.rss)                                                   | https://www.jodimckay.com.au/media_releases                                        |
| [NT Government Newsroom](https://newsroom.nt.gov.au/api/RSS/NewsroomIndex)                                                                           | https://newsroom.nt.gov.au/                                                        |
| [NT Government Departmental and Agency Media Releases](https://mediareleases.nt.gov.au/api/RSS/MediaReleasesIndex)                                   | https://mediareleases.nt.gov.au/                                                   |
| [ACT Government RSS Feed Collection](https://www.cmtedd.act.gov.au/open_government/inform/act_government_media_releases/all_media_release_rss_feeds) | https://www.cmtedd.act.gov.au/open_government/inform/act_government_media_releases |

## Projects used

- [scrapy](https://github.com/scrapy/scrapy)
- [scrapy-rss](https://github.com/woxcab/scrapy_rss)
- [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)
- [splash](https://github.com/scrapinghub/splash)

---

Copyright (c) 2021 Callum Skeet under [MIT License](./LICENSE)
