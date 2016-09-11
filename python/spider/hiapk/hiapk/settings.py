# -*- coding: utf-8 -*-

# Scrapy settings for hiapk project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hiapk'

SPIDER_MODULES = ['hiapk.spiders']
NEWSPIDER_MODULE = 'hiapk.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hiapk (+http://www.yourdomain.com)'

#禁止cookies,防止被ban
COOKIES_ENABLED = False
COOKIES_ENABLES = False

#设置Pipeline,此处实现数据写入文件
ITEM_PIPELINES = {
    'hiapk.pipelines.HiapkPipeline':300
}

#设置爬虫爬取的最大深度
DEPTH_LIMIT=100

#取消默认的useragent,使用新的useragent
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'hiapk.spiders.rotate_useragent.RotateUserAgentMiddleware' :400
    }
