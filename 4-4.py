#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/17

def f1(i):
    '''
    返回 i/2 的值
    :param i: int
    :return: float, i/2 的值
    '''
    return i/2

def f2(i):
    '''
    返回 i*4 的值
    :param i: float
    :return: float, i*4 的值
    '''
    return i*4

x = int(input('请输入：'))

a = f1(x)
print(a)

b = f2(a)
print(b)