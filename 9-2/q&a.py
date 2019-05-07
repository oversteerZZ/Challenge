#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/21

height = input('你的身高是多少？')

with open('height.txt', 'w') as f:
    f.write('{}cm'.format(height))
