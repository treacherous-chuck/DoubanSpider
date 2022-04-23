# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:09:11 2022

@author: 95118
"""

import tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
from utils import *

def onclick(x):
     k=int(x)
     if(k==0):
         tkinter.messagebox.showinfo('提示','您输入的值无效！')
     else:
         url = "https://movie.douban.com/top250"
         headers = {
         "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"
                 }
         resp=requests.get(url,headers=headers)
         page_content=resp.text

         obj = re.compile(
             r'<li>.*?<div class="item">.*?<span class="title">(?P<电影名>.*?)'
             r'</span>.*?<p class="">.*?<br>(?P<年份>.*?)&nbsp.*?'
             r'<span class="rating_num" property="v:average">(?P<评分>.*?)</span>'
             r'.*?<span>(?P<评价人数>.*?)人评价</span>', re.S)

         ret = obj.finditer(page_content)
         k=int(x)
         i=1
         for it in ret:
             if(i==k):
                 canvas_root.create_text(15, 500, 
                                         text = '电影名：%s\n年份：%s\n评分：%s\n评价人数：%s'%(it.group("电影名"),it.group("年份").strip(),it.group("评分"),it.group("评价人数")),
                                         font=('楷体',15),
                                         fill='DodgerBlue',
                                         anchor = W,
                                         justify = LEFT)
                 break
             else:
                 i=i+1
     
root=tkinter.Tk()
root.title('豆瓣电影信息提取器')
root.config(bg='#8DB6CD')#窗口内部全部设为淡蓝色
root.geometry('600x600+300+30')
root.resizable(True,True)#用户可不可以调整窗口大小
root.iconbitmap('small_logo.ico')#左上角加logo

#画布内设为白色
cv = tkinter.Canvas(root,bg='white')

#设置背景图片
w=600
h=600
canvas_root=tkinter.Canvas(root,width=w,height=h)
im_root=get_image('background.jpg',w,h)
canvas_root.create_image(w/2,h/2,image=im_root)
canvas_root.pack()

#label
canvas_root.create_text(15, 403, text = '请输入要查询的名次:',
                        font=('楷体',15),
                        fill='DodgerBlue',
                        anchor = W,
                        justify = LEFT)
#输入框
inp = Entry(root)
inp.place(relx=0.35, rely=0.65, relwidth=0.15, relheight=0.05)


#为按钮设置背景图片
butt=tkinter.Button(root,text='查询',
                      fg='DodgerBlue',
                      font=('楷体',15),
                      background='seashell',
                      compound=tkinter.CENTER,
                      command=lambda: onclick(inp.get()))
butt.place(x=320,y=390,width=80,height=30)




root.mainloop()
