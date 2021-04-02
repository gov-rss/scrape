<h1 align="center"><b>gov-scrape</b></h1>
<h3 align="center"><b>RSS feeds from government media releases</b></h3>
<p align="center">
    <i>gov + RSS</i>
</p>

---

<br>

A collection of Scrapy spiders that transform government media releases into
RSS feeds. The purpose of creating this is to increase the availability of these media releases to members of the public, making it easier to keep up to date with state governments.

## Setup

### Pip

```shell
$ pip install -r requirements.txt
```

### Conda

```shell
$ conda create --file=environment.yaml
$ conda activate gov-scrape
```

### Docker

```shell
$ docker build --rm -t gov-scrape .
```

## Run

### Shell

```shell
$ scrapy crawl <spider-name>  # one spider
$ ./crawl.sh                  # all spiders
```

### Docker-Compose

```shell
$ docker-compose run gov-scrape
```

### Docker

```shell
$ docker run \
    --name gov-scrape \
    --rm \
    -v $FEED_DIR:/gov-scrape/feeds \    # stores rss files
    -v $LOG_DIR:/gov-scrape/logs \      # log files from scrapy
    -it gov-scrape                      # crawls with all spiders
```

The regular shell commands also work with Docker, e.g. `scrapy crawl vic-prem` can be passed to the container.

### Available spiders

| Spider Name                                             | Source                                                                             |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [act_shadow](./gov_scrape/spiders/act_shadow_spider.py) | [canberraliberals.org.au](https://canberraliberals.org.au/news)                    |
| [nsw_gov](./gov_scrape/spiders/nsw_gov_spider.py)       | [nsw.gov.au](https://www.nsw.gov.au/news)                                          |
| [nsw_prem](./gov_scrape/spiders/nsw_prem_spider.py)     | [nsw.gov.au](https://www.nsw.gov.au/media-releases)                                |
| [nt_shadow](./gov_scrape/spiders/nt_shadow_spider.py)   | [countryliberal.org](http://www.countryliberal.org/)                               |
| [sa_prem](./gov_scrape/spiders/sa_prem_spider.py)       | [premier.sa.gov.au](https://www.premier.sa.gov.au/news/media-releases)             |
| [tas_prem](./gov_scrape/spiders/tas_prem_spider.py)     | http://www.premier.tas.gov.au/media_release_search?queries_portfolio_query=Premier |
| [qld_gov](./gov_scrape/spiders/qld_gov_spider.py)       | https://statements.qld.gov.au/                                                     |
| [qld_shadow](./gov_scrape/spiders/qld_shadow_spider.py) | https://www.lnp.org.au/news/                                                       |
| [sa_shadow](./gov_scrape/spiders/sa_shadow_spider.py)\* | https://www.facebook.com/SouthAustralianLabor/                                     |
| [tas_shadow](./gov_scrape/spiders/tas_shadow_spider.py) | https://taslabor.com/news/                                                         |
| [vic_prem](./gov_scrape/spiders/vic_prem_spider.py)     | https://www.premier.vic.gov.au/media-centre                                        |
| [vic_shadow](./gov_scrape/spiders/vic_shadow_spider.py) | https://vic.liberal.org.au/MediaReleases/                                          |
| [wa_gov](./gov_scrape/spiders/wa_gov_spider.py)         | https://www.mediastatements.wa.gov.au/Pages/Default.aspx                           |
| [wa_shadow](./gov_scrape/spiders/wa_shadow_spider.py)   | https://www.waliberal.org.au/news/                                                 |

_\* In the process of getting permission from Facebook to scrape the SA Labor page_

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

Copyright (c) 2021 [Callum Skeet](https://github.com/callumskeet) under the [MIT License](./LICENSE)

```

```
