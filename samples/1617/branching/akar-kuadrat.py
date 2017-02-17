# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:59:09 2017

@author: Abdul Munif
"""
import math

a = input('a: ')
b = input('b: ')
c = input('c: ')

determinan = b**2 - 4*a*c
if determinan >= 0:
    x1 = (-b + math.sqrt(determinan))/(2*a)
    x2 = (-b - math.sqrt(determinan))/(2*a)
    print x1, x2
else:
    print "Undefined"