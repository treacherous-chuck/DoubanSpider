# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:33:08 2022

@author: 95118
"""

import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from utils import *

root=tkinter.Tk()
root.title('豆瓣电影信息提取器')
root.config(bg='#8DB6CD')#窗口内部全部设为淡蓝色
root.geometry('1000x600+130+10')
root.resizable(True,True)#用户可不可以调整窗口大小
root.iconbitmap('small_logo.ico')#左上角加logo

#画布内设为白色
cv = tkinter.Canvas(root,bg='white')

#设置背景图片
w=1000
h=600
canvas_root=tkinter.Canvas(root,width=w,height=h)
im_root=get_image('background.jpg',w,h)
canvas_root.create_image(w/2,h/2,image=im_root)
canvas_root.pack()



#为Label组件设置图片
lbImage=tkinter.Label(root,text='是否在本地下载豆瓣20个高分电影海报？',
                      fg='blue',
                      font=('隶书',20),
                      background='#000000',
                      compound=tkinter.CENTER)
lbImage.place(x=150,y=150,width=500,height=80)



#为按钮设置背景图片
btn0k=tkinter.Button(root,text='确定',
                     fg='blue',
                     font=('隶书',15),
                     background='#333333',
                     compound=tkinter.CENTER,
                     command=onclick)
btn0k.place(x=330,y=300,width=100,height=50)

root.mainloop()





