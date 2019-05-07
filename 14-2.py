#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/24


class Square:
    square_list = list()

    def __init__(self, length):
        self.length = length
        self.square_list.append(self.length)

    def __repr__(self):
        return '{} by {} by {} by {}'.format(self.length,
                                             self.length,
                                             self.length,
                                             self.length,
                                             )


squ1 = Square(29)
print(squ1)