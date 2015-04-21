# -*- coding: utf-8 -*-

# Scrapy settings for jdbook project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jdbook'

SPIDER_MODULES = ['jdbook.spiders']
NEWSPIDER_MODULE = 'jdbook.spiders'

ITEM_PIPELINES = {
    'jdbook.pipelines.JsonWriterPipeline': 800,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jdbook (+http://www.yourdomain.com)'
