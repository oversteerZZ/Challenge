#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/24


class Shape:
    def what_am_i(self):
        print('I\'m a shape')


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return (self.length + self.width) * 2


class Square(Shape):

    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        return self.length * 4

    def change_size(self, change):
        self.length = self.length + change


rec1 = Rectangle(3, 4)
squ1 = Square(3)
rec1.what_am_i()
squ1.what_am_i()
