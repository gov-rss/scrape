#!/bin/bash

# start splash
su splash -c "python3 /app/bin/splash \
    --proxy-profiles-path /etc/splash/proxy-profiles \
    --js-profiles-path /etc/splash/js-profiles \
    --filters-path /etc/splash/filters \
    --lua-package-path /etc/splash/lua_modules/?.lua" &> ./logs/splash.log &


for SPIDER in $(scrapy list); do
    echo -n "Running $SPIDER spider..."
    scrapy crawl --logfile=logs/${SPIDER}.log --loglevel=ERROR $SPIDER
    echo "finished"
    break
done