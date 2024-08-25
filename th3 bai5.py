# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:11:08 2024

@author: Dell
"""

a = int(input("Nhập giờ: "))

b = int(input("Nhập phút: "))

c = int(input("Nhập giây: "))

sh = a*3600
sp = b*60
tt = sh + sp + c

print("Nhập kết quả đổi ra giây:", tt)