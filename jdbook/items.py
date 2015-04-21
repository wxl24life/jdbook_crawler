# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdbookItem(scrapy.Item):
    # define the fields for your item here like:
    publication_by = scrapy.Field()
    isbn_num = scrapy.Field()
    book_name = scrapy.Field()
    publication_time = scrapy.Field()
