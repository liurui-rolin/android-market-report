# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

'''
这是记录每一个应用的信息
'''
class PageItem(Item):
    #-----------------------------页面基本信息
    #当前url
    url = Field()
    #大类
    class1 = Field()
    #小类
    class2 = Field()
    #logo
    logo_url = Field()
    #应用名称
    title = Field()
    #版本
    version = Field()
    #屏幕截图
    screenshot = Field()
    #简介
    intro = Field()

    #-----------------------------用户评价
    #评分
    score = Field()
    #评分人数
    score_person_num = Field()
    #评分详情
    score_detail = Field()
    #评分标签: 好
    score_tag = Field()
    #评论数
    score_count = Field()
    #评论首页
    score_content = Field()

    #-----------------------------作者/应用信息
    #作者
    author = Field()
    #热度
    hot = Field()
    #大小
    size = Field()
    #语言
    language = Field()
    #固件
    firmware = Field()
    #支持屏幕
    screen = Field()
    #上架时间
    up_time = Field()

    #-----------------------------其他
    #热点资讯
    hot_consult = Field()
    #相关推荐
    recommend = Field()
    #其他版本
    other_version = Field()


