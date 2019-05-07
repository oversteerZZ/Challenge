#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/24


class Horse:

    def __init__(self, name, gender, rider):
        self.name = name
        self.gender = gender
        self.rider = rider


class Rider:

    def __init__(self, name):
        self.name = name


person1 = Rider('LvBu')
print(person1.name)
horse1 = Horse('Red Rabbit', 'male', person1)
print(horse1.rider.name)
