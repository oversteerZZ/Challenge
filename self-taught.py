#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# author:茁
# date:2019/4/21
import csv

with open('st.txt', 'r') as f:
    r = csv.reader(f, delimiter=',')
    for row in r:
        print(",".join(row))