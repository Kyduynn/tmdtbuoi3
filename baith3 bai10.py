# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:34:49 2024

@author: Dell
"""

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

A = (a**(1/2)-b**(1/2) / a**(1/4)-b**(1/4)) + (a**(1/2)+a*b**(1/4) / a**(1/4)+b**(1/4))
print("Kết quả:", A)