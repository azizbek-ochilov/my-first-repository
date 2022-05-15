# -*- coding: utf-8 -*-
"""
Created on Sat May 14 09:36:55 2022

@author: hp
"""
# AMALIYOT
#- Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#ismlar = ["Azizbek", "Lazizbek", "Madina", "Behruz", "Nodira"]
#for ism in ismlar:
 #   print(f" Assalomu alaykum {ism}")
#- Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
#print(f"Elementlar soni {len(ismlar)} ga teng.")
#- 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
sonlar = list(range(11, 100,2))
#for son in sonlar:
#    print(f"{son}ining kubi {son**3}ga teng.")
#- Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#kinolar = []
#print(f"Sevimli kinolaringizni kiriting:")
#for k in range(5):
 #   kinolar.append(input(f"{k+1}-kino:"))
  #  print(kinolar)

#- Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va 
#har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odamlar = []
n_odam = int(input(f"Bugun nechta odam bilan suhbatlashdingiz?"))
for M in range(n_odam):
    odamlar.append(input(f"{M+1}- do'stingiz:"))
    print(odamlar)
    