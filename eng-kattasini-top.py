# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:27:51 2022

@author: hp
"""

print("Siz kiritgan 5 ta son ichida eng kattasini topib beraman")
sonlar = []
sonlar.append(float(input("1-son\n>>>")))
sonlar.append(float(input("2-son\n>>>")))
sonlar.append(float(input("3-son\n>>>")))
sonlar.append(float(input("4-son\n>>>")))
sonlar.append(float(input("5-son\n>>>")))
print(f"Eng katta son bu {max(sonlar)}")