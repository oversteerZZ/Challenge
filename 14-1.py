#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/24


class Square:
    square_list = list()

    def __init__(self, length):
        self.length = length
        self.square_list.append(self.length)


squ1 = Square(4)
squ2 = Square(5)
print(Square.square_list)
