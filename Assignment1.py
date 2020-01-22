#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 21:38:16 2020

@author: Jonas
Assignment 1
"""


#money = input("Enter a Amount of Money to Compound  ")

#print("The Amount ", money)

P = float(input("Enter starting principle please. "))
n = 12
r = 0.05
t = 10

final = round(P * ((1 + (.05/n) )** (n*t)), 2)
print("The final amount after", t, "years is ", final)