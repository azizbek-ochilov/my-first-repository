# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:37:45 2022

@author: hp
"""
#VAZIFA1
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
#alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
 
#python_izohli_lugati = {"float":"matinni son ko'rinshida oladi", "integer":"matinni butun son ko'rinishiad qabul qiladi", "string":"matn", "if":"agar",
#          "else":"yo'qsa", "elif":"mabodo", "title":"bosh xarf", "upper":"katta harf", "reverse":"teskari","for in":"ichida", "and":"va" }
#for n, m in sorted(python_izohli_lugati.items()):
#    print(f" {n} bu {m}")

#VAZIFA2
#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
#alifbo ketma-ketligida konsolga chiqaring.

#d = {"o'zbekiston":'toshkent','rossiya':'maskva','aQSH':'vashington',"qozog'iston":"nursulton","turkiya":"anqara"}
#for a , b in sorted(d.items()):
#     if a.lower() == "aqsh" : print(f"AQSHning poytaxti - {b.title()}.")
#     else: print(f"{a.title()}ning poytaxti - {b.title()}. ")


#VAZIFA3
#Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
#Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.


#d = {"o'zbekiston":'toshkent','rossiya':'maskva','aQSH':'vashington',"qozog'iston":"nursulton","turkiya":"anqara"}
#davlat = input("Poytaxtini topish zarur bo'lgan davlat nomini kiriting\n>>>").lower()
#c = d.get(davlat)    
#if c ==None  : print("Bizda bunday ma'lumot hozirda mavjud emas!")
#else: print(f" {davlat.title()}ning poytaxti - {c.title()}.")


#VAZIFA4
#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
#Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda
# "bizda bunday taom yo'q" degan xabarni chiqaring
menu = {"osh": 25000,
        "sho'rva": 15000,
        "salat": 5000,
        "choy": 2000,
        "non": 3000,
        "kabob": 6000,
        "lag'mon": 13000,
        "lavash": 18000,
        "somsa": 6000,
        "gril": 16000}
print("Haridorlar ko'pligi sababdan 3 ta ovqatga buyurtma berishingiz mumkin. ")
zakaz = []
for n in range(3):
    zakaz.append(input(f"{n+1}-siga nima aytasiz?>>>"))
  
for bor in zakaz:     
    if bor in menu : print(f"Siz kiritgan {bor} bizda mavjud.")
    else:print(f" {bor.title()} hozirda mavjud emas.  ")






