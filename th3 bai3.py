# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:39:50 2024

@author: Dell
"""

a = int(input("Nhập số thứ nhất:" ))

b = int(input("Nhập số thứ hai:" ))

t = (a + b)
h = (a - b)
tich = (a * b)
thuong = (a / b)
round(thuong,3)
cld = a%b
cln = a//b

print("Tổng là:", t)
print("Hiệu là:", h)
print("Tích là:", tich)
print("Thương là:", thuong)
print("Chia lấy dư:", cld)
print("Chia lấy nguyên:", cln) 
