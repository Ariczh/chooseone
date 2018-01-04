#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from sys import exit
from random import choice
import tkinter

teas = ['温润红茶','乌龙茶','英式早餐茶']
tea = choice(teas)

wind = tkinter.Tk()
wind.resizable(False, False)
wind.title('今天喝什么茶')
wind.geometry('300x150')

on_hit = False  # 默认初始状态为 False
def exhit():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        exit()

te = tkinter.Label(wind, text=tea, width=15, height=4, font=('Microsoft Yahei', 12))
te.pack()

bu = tkinter.Button(wind, text = '确定', width=15, height=2, font=('Microsoft Yahei', 10), command=exhit)
bu.pack()

wind.mainloop()
