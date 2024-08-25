# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:53:36 2024

@author: Dell
"""
N = int(input("Nhập số nguyên có 2 chữ số: "))

if N>=10 and N<=99: 

    pd = N%10
    pn = N//10
    S = pd + pn
    
    print("Tổng các số là:", S)