#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/5/6

import re

string = 'The ghost that says boo haunts the loo.'

word = re.findall('[bl]oo', string)

print(word)
