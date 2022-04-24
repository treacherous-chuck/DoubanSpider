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
    
MOV = Movies()
MOV=init(MOV)

root=tkinter.Tk()
root.title('豆瓣电影信息提取器')
root.config(bg='seashell')#窗口内部全部设为淡蓝色
root.geometry('600x600+300+30')
root.resizable(False,False)#用户可不可以调整窗口大小
root.iconbitmap('small_logo.ico')#左上角加logo

#设置背景图片
w=600
h=400
canvas_root=tkinter.Canvas(root,width=w,height=h)
im_root=get_image('background.jpg',w,h)
canvas_root.create_image(w/2,h/2,image=im_root)
canvas_root.pack()

#label
canvas_root.create_text(100, 50, text = '请输入要查询的电影的名次:',
                        font=('楷体',15),
                        fill='DodgerBlue',
                        anchor = W,
                        justify = LEFT)
#输入框
inp = Entry(root)
inp.place(x=360, y=36, width=70, height=25)

im=get_image("./Top250_movie_images/" + MOV.id[0][0] + "_" + 
              MOV.title[0][0] + '.jpg',216,320)

#按钮
butt1=tkinter.Button(root,text='查询',
                      fg='DodgerBlue',
                      font=('楷体',15),
                      background='seashell',
                      compound=tkinter.CENTER,
                      command=lambda: search(inp.get(),MOV))
butt1.place(x=460,y=36,width=70,height=25)

#输出框
t = tkinter.Text(width=40,height=12)
t.pack()

def search(x,MOV):
    global im
    d=int(x)-1;
    if(d<0 or d>249):
        t.delete('1.0','end')
        tkinter.messagebox.showinfo('提示','请输入1至250之间的整数！')
    else:
        t.delete('1.0','end')
        d=int(x)-1;
        im=get_image("./Top250_movie_images/" + MOV.id[d][0] + "_" + 
                     MOV.title[d][0] + '.jpg',216,320)
        canvas_root.create_image(300,240,image=im)
        canvas_root.pack()
        t.insert('end', 
                 '片名：%s\n\n排名：%s\n\n评分：%s\n\n简述：%s'%(
                     MOV.title[d][0],
                     MOV.id[d][0],
                     MOV.score[d][0],
                     MOV.desc[d][0]))

root.mainloop()
