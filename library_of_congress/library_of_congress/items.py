# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LibraryOfCongressItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    marc_url = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
