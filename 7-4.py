#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/21
number_list = [2, 4, 5, 54, 23, 98, 101]
while True:
    number = input('请输入：')
    if number == 'q':
        break
    else:
        yes_flag = False
        for i in number_list:
            if int(number) == i:
                print('你猜对了')
                yes_flag = True
                break
        if yes_flag == False:
            print('你猜错了')