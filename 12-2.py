#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/23

import math


class Circle:
    def __init__(self, d):
        self.diameter = d

    def area(self):
        return (self.diameter/2)**2*math.pi


circle1 = Circle(5)
print(circle1.area())
