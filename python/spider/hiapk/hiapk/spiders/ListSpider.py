#-*-coding:utf-8-*-
import scrapy
import sys
import time
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from hiapk.items import PageItem

reload(sys)
sys.setdefaultencoding("utf-8")

class ListSpider(CrawlSpider):
    #爬虫名称
    name = "ListSpider"
    #设置下载延时
    download_delay = 2
    #允许域名
    allowed_domains = ["hiapk.com"]
    #开始URL
    start_urls = [
        "http://apk.hiapk.com/apps?sort=5&pi=1"
    ]
    #爬取规则,不带callback表示向该类url递归爬取
    rules = (
        Rule(LinkExtractor(allow=('apps?sort=5&pi=[0-9]+', ))),
        Rule(LinkExtractor(allow=('appinfo/*', )), callback='parse_content'),
    )

    #解析内容函数
    def parse_content(self, response):
        item = PageItem()

        #当前URL
        #print response.url
        item['url'] = response.url
        #大类
        item['class1'] = response.selector.xpath("//a[@id='categoryParent']/text()")[0].extract().decode('utf-8')
        #小类
        item['class2'] = response.selector.xpath("//a[@id='categoryLink']/text()")[0].extract().decode('utf-8')
        #logo
        item['logo_url'] = response.selector.xpath("//div[@class='detail_content']/div[@class='left']/img/@src")[0].extract().decode('utf-8')
        #应用名称
        title_verson = response.selector.xpath("//div[@id='appSoftName']/text()")[0].extract().decode('utf-8').replace('\n','').strip()
        item['title'] = title_verson[0:title_verson.find('(')]
        #版本
        item['version'] = title_verson[title_verson.find('(')+1:title_verson.rfind(')')]
        #屏幕截图
        slist = []
        for imga in response.selector.xpath("//ul[@id='screenImgUl']/li"):
            slist.append(imga.xpath("a/@href")[0].extract().decode('utf-8'))
        item['screenshot'] = slist
        #简介
        item['intro'] = response.selector.xpath("//pre[@id='softIntroduce']/text()")[0].extract().decode('utf-8').replace('\n','').strip()



        yield item
