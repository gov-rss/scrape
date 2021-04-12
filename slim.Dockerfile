FROM python:3.8.8-slim

RUN apt update
RUN apt upgrade -y

WORKDIR /gov-scrape

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir feeds
RUN mkdir logs

COPY . .
RUN chmod +x crawl.sh

ENTRYPOINT [ "bash", "-c" ]
CMD [ "/gov-scrape/crawl.sh" ]