#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/23

class Hexagon:

    def __init__(self, a):
        self.side = a

    def calculate_perimeter(self):
        return self.side*6


hex1 = Hexagon(4)
print(hex1.calculate_perimeter())
