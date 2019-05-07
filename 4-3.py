#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/17

def five(a, b, c, d=4, e=3):
    '''
    返回 a+b+c+d+e 的值
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :param e: int
    :return: int, a+b+c+d+e 的和
    '''
    return a+b+c+d+e

print(five(2,3,4,5,6))