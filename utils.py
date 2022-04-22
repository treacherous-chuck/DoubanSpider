# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 14:22:57 2022

@author: 95118
"""
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk

import requests
import jsonpath
from urllib.request import urlretrieve
import os
import time

def url_list(id):
    #目标url
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start={}'.format(id)
    #模拟浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    #发送请求,解析json数据
    req = requests.get(url, headers=headers).json()
    #查找图片和名字
    data_list = jsonpath.jsonpath(req, '$..cover')#图片的网址
    name_list = jsonpath.jsonpath(req, '$..title')#图片的名字
    #返回数据
    return (data_list,name_list)

def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

def onclick():
    tkinter.messagebox.showinfo('提示','您单击了确定按钮')
    #文件夹名
    text='豆瓣高评分图片'
    #判断文件夹是否创建
    if not os.path.exists(text):
        os.mkdir(text)
    #这里我只要300张图片
    for i in range(0,20,20):#i=0,20,40,...,280,300
        #获取图片链接
        link_list,names = url_list(i)
        #保存数据
        for link,name in zip(link_list,names):
            #防止报错
            try:
                #到哪个链接查找，然后是哪个文件夹和里面的名字,后缀是.什么的格式
                urlretrieve(link,text+'/'+name+'.jpg')
                #打印成功
                print(name+'100%')
            except:
                pass