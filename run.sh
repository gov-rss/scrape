#!/usr/bin/bash

for SPIDER in $(scrapy list); do
    echo -n "Running $SPIDER spider..."
    scrapy crawl --logfile=logs/${SPIDER}.log --loglevel=ERROR $SPIDER
    echo "finished"
done