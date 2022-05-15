# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:27:01 2022

@author: hp
"""

#cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort()
#print(cars)




# VAZIFA1  O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#davlatlar = ["O'zbekiston", "Qozoqiston", "Armanston"]
#print(davlatlar)

# VAZIFA2 Ro'yxatning uzunligini konsolga chiqaring
#print(len(davlatlar))

#VAZIFA3 sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#davlatlar = sorted(davlatlar)
#print(davlatlar)

#VAZIFA4 sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#davlatlar = sorted(davlatlar, reverse=True)
#print(sorted(davlatlar, reverse=True))

#VAZIFA Asl ro'yxatni qaytadan konsolga chiqaring
#print(davlatlar)

#VAZIFA reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#davlatlar.reverse()
#print(davlatlar)

#VAZIFA sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
#davlatlar.sort()
#print(davlatlar)
#davlatlar.sort(reverse=True)
#print(davlatlar)

#VAZIFA 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#sonlar = list(range(120,1201, 2))
#print(sum(sonlar))
#print(max(sonlar)-min(sonlar))
#print(len(sonlar))
#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

#print(sonlar[:20])
#print(sonlar[530:550])
#print(sonlar[-20:])

#VAZIFA taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["palov", 'shashlik', "shaurma", "dimlama"]
nonushta = taomlar[:]
taomlar.remove("shashlik")
taomlar.remove("shaurma")
taomlar.append("sasiska")
taomlar.append("tuxum")
print(taomlar)
print(nonushta)

#VAIFA Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)
nonushta[0] = "qaymoqva non"












