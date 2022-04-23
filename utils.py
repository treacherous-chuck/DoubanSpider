# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:10:08 2022

@author: 95118
"""

import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image,ImageTk
import requests
import jsonpath
from urllib.request import urlretrieve
import os
import time
import re


def get_image(filename,width,height):
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

