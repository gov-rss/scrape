FROM scrapinghub/splash:master

USER root

WORKDIR /gov-scrape

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/home/splash/.local/bin:${PATH}"

RUN mkdir feeds
RUN mkdir logs

COPY . .
RUN chmod +x ./run.sh

ENTRYPOINT [ "/gov-scrape/run.sh" ]
