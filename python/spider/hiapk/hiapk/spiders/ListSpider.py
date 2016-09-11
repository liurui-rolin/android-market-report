#-*-coding:utf-8-*-
import scrapy
import sys
import time
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
from meishi.items import MeishiItem

reload(sys)
sys.setdefaultencoding("utf-8")

class ListSpider(CrawlSpider):
    #爬虫名称
    name = "ListSpider"
    #设置下载延时
    download_delay = 2
    #允许域名
    allowed_domains = ["meishichina.com"]
    #开始URL
    start_urls = [
        "http://home.meishichina.com/recipe/liangcai/#utm_source=recipe_index_tags_type"
    ]
    #爬取规则,不带callback表示向该类url递归爬取
    rules = (
        Rule(LinkExtractor(allow=('page/[0-9]+', ))),
        Rule(LinkExtractor(allow=('recipe-[0-9]+', )), callback='parse_content'),
    )

    #解析内容函数
    def parse_content(self, response):
        item = MeishiItem()

        #当前URL
        #print response.url
        item['url'] = response.url

        #菜谱标题
        title = response.selector.xpath("//div[@class='recipDetail']/input[@id='recipe_title']/@value")[0].extract().decode('utf-8')
        print title
        item['title'] = title

        #菜谱主图URL
        img_url = response.selector.xpath("//div[@class='recipDetail']/div[@id='recipe_De_imgBox']/a[@class='J_photo']/img/@src")[0].extract().decode('utf-8')
        #print img_url
        item['img_url'] = img_url

        #获取菜谱配料
        detail = []
        mts = response.selector.xpath("//div[@class='recipDetail']/div[@class='recipeCategory clear']/div[@class='recipeCategory_sub clear']")
        for sel in mts:
            temp_map = {}
            mt = sel.xpath("div")
            mt_l = mt[0].xpath("text()")[0].extract().decode('utf-8')
            temp_map['key'] = mt_l
            s1 = ""
            for mt_r in mt[1].xpath("ul/li | div | div/a "):
                s1 = "%s\t%s %s" % (s1 , "".join([ ss.extract().decode('utf-8').replace(" ","").replace("\t","").replace("\r\n","") for ss in mt_r.xpath("span[@class='category_s1']/a/text() | span[@class='category_s1']/text() | text() ") ]) , "".join([ ss.extract().decode('utf-8').replace(" ","").replace("\t","").replace("\r\n","") for ss in mt_r.xpath("span[@class='category_s2']/text()")]) )
            #print s1
            temp_map['value'] = s1
            detail.append(temp_map)
        item['detail'] = detail

        #获取步骤
        steps_list = []
        steps = response.selector.xpath("//div[@class='recipDetail']/div[@class='recipeStep']/ul/li")
        for sel in steps:
            s_url = "%s" % ( "".join( [ ss.extract().decode('utf-8').replace(" ","").replace("\t","").replace("\r\n","") for ss in sel.xpath("div[@class='recipeStep_img']/img/@src")])  )
            s_content = "%s" % ( "".join( [ ss.extract().decode('utf-8').replace(" ","").replace("\t","").replace("\r\n","").strip() for ss in sel.xpath("div[@class='recipeStep_word']/text()")])  )
            #print "%s:%s" % (s_content,s_url)
            steps_list.append("%s\t%s" % (s_content,s_url))
        item['steps'] = steps_list

        yield item
