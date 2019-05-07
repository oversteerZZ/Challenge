#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/24


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return (self.length+self.width)*2


class Square:

    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        return self.length*4


rec1 = Rectangle(3, 4)
squ1 = Square(3)
print(rec1.calculate_perimeter())
print(squ1.calculate_perimeter())