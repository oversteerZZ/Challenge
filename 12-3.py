#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/23

import math


class Triangle:

    def __init__(self, a, b, c):
        if a > b + c or b > a + c or c > a + b:
            print('That can\'t be a triangle!')
        else:
            self.side1 = a
            self.side2 = b
            self.side3 = c

    def area(self):
        p = (self.side1+self.side2+self.side3)/2
        s = math.sqrt(p*(p-self.side1)*(p-self.side2)*(p-self.side3))
        return s


triangle1 = Triangle(2, 2, 2)
print(triangle1.area())
