#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/16

age = int(input('请输入年龄：'))

if age < 2:
    print('baby')
elif age >= 2 and age < 13:
    print('kid')
elif age >= 13 and age < 18:
    print('youth')
elif age >= 18 and age < 30:
    print('adult')
else:
    print('grown-up')

