#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/17

def f(i):
    '''
    返回 float(i) 的值
    :param i: int,float
    :return: float, i转换为浮点数的值
    '''
    return float(i)

x = input('请输入：')

try:
    print(f(x))
except(ValueError):
    print('请输入纯数字')