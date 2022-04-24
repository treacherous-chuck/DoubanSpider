# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:10:08 2022

@author: 95118
"""
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
import requests
import jsonpath
from urllib.request import urlretrieve
import os
import re
from lxml import etree
from collections import Iterable
from collections import Iterator

class Movies(object):
    """定义一个电影类"""

    def __init__(self):
        self.id = list()
        self.title = list()
        self.score = list()
        self.desc = list()
        self.img_addr = list()
        self.num = 0

    def addid(self, id):
        self.id.append(id)

    def addtitle(self, title):
        self.title.append(title)

    def addscore(self, score):
        self.score.append(score)

    def adddesc(self, desc):
        self.desc.append(desc)

    def addimg_addr(self, img_addr):
        self.img_addr.append(img_addr)

    def __iter__(self):
        return self   # 返回本身

    def __next__(self):
        if self.num < len(self.id):
            ret = self.title[self.num]
            self.num += 1
            return ret

        # 抛出异常，当循环后自动结束
        else:
            raise StopIteration

# 获取图片
def get_image(filename, width, height):
    im = Image.open(filename).resize((width, height))
    return ImageTk.PhotoImage(im)

# 负责下载电影海报
def download_img(db_id, title, img_addr, headers):

    # 如果不存在图片文件夹,则自动创建
    if os.path.exists("./Top250_movie_images/"):
        pass
    else:
        os.makedirs("./Top250_movie_images/")

    # 获取图片二进制数据
    image_data = requests.get(img_addr, headers=headers).content
    # 设置海报存存储的路径和名称
    image_path = "./Top250_movie_images/" + db_id[0] + "_" + title[0] + '.jpg'
    # 存储海报图片
    with open(image_path, "wb+") as f:
        f.write(image_data)

def init(MOV):
    # 使用列表生成式,生成待爬取的页面url的列表
    urls = ["https://movie.douban.com/top250?start=" +
            str(i*25) for i in range(10)]

    # 设置请求头
    headers = {
        # 设置用户代理头
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    # 为避免重复运行程序,造成内容重复,这里把上次的文件清除(可跳过)
    if os.path.isfile("./douban_movie_top250.txt"):
        os.remove("./douban_movie_top250.txt")

    # 从列表取出url进行爬取
    for url in urls:
        # 获取页面的响应内容
        db_response = requests.get(url, headers=headers)

        # 将获得的源码转换为etree
        db_reponse_etree = etree.HTML(db_response.content)

        # 提取所有电影数据
        db_movie_items = db_reponse_etree.xpath(
            '//*[@id="content"]/div/div[1]/ol/li/div[@class="item"]')

        # 遍历电影数据列表,
        for db_movie_item in db_movie_items:

            # 这里用到了xpath的知识
            db_id = db_movie_item.xpath('div[@class="pic"]/em/text()')
            db_title = db_movie_item.xpath(
                'div[@class="info"]/div[@class="hd"]/a/span[1]/text()')
            db_score = db_movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')
            db_desc = db_movie_item.xpath(
                'div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
            db_img_addr = db_movie_item.xpath('div[@class="pic"]/a/img/@src')
            MOV.addid(db_id)
            MOV.addtitle(db_title)
            MOV.addscore(db_score)
            MOV.adddesc(db_desc)
            MOV.addimg_addr(db_img_addr)
            print("已加载100%:", str(db_id)[2:-2], ".", str(db_title)[2:-2])
            #print("编号:",db_id,"标题:",db_title, "评分:",db_score,"电影描述:", db_desc)

            db_img_addr = str(db_img_addr[0].replace("\'", ""))
            download_img(db_id, db_title, db_img_addr, headers)
    return MOV
