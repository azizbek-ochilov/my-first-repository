# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:45:45 2022

@author: hp
"""

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
#for car in cars:
    # if car == "gm":
   #      print(car.upper())
  #   else:
 #         print(car.title()) 


#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
#for car in cars:
  #  if car != "gm":
  #      print(car.title())
 #   else: print(car.upper())    
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
#xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
#ism = input(f"Assalomu alaykum ismining nima?\n>>>")
#if ism.lower() == "admin":
 #   print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
#else: print(f" Xush kelibsiz, {ism.title()}!")    

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
#print(f" Siz menga a va b sonlar qiymatini kiriting men sizga ularni tengligini ko'rsataman ")
#a = int(input(f" a sonni kiriting:"))
#b = int(input(f" b sonni kiriting:"))
#if a==b : print(f"Siz kiritgan sonlar bir biriga teng")
#else: print(f"Siz kiritgan sonlar bir biridan faq qiladi.")
#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", 
#agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = int(input(f"Istalgan sonni kiriting:\n>>>"))
if son < 0 : print(f"Siz kiritgan {son} soni manfiy")
if son == 0 : print(f"Siz kiritgan {son} soni 0 ga teng. Musbat ")
if son > 0 : print(f"Siz kiritgan {son} soni musbat.")
if son == str(son): print("Iltimos son kiriting>") 


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring

a = float(input(f"Ildizini hisoblash kerak bo'lgan sonni kiriting:\n>>>"))
if a > 0: print(f"Siz kiritgan {a} sonning ildizi {a**(1/2)}ga teng.")
else: print(f"Iltimos musbat sonni kiriting. Chunki, manfiy sonning ildiz mavjud emas!!!")



