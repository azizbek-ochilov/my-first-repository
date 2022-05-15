# -*- coding: utf-8 -*-
"""
Created on Sat May 14 16:02:56 2022

@author: hp
"""

# AMALIYOT

### Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

#- Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" 
#degan xabarni chiqaring
#son = float(input(f"Juft sonni kiriting:\n>>>"))
#if son%2:
 #   print('Bu son juft emas.')
#else:
#    print("Rahmat!")
    
    
#- Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#    + Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#    + Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#    + Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
#yosh = int(input(f"Chipta narxini bilish uchun yoshingizni kiriting:\n >>> "))
#f yosh <=0 : narx=0 ,print("Yoshingizni to'g'ri kiriting") 
#elif yosh < 4: narx=4000
#elif yosh < 18: narx= 10000
#else: narx= 20000
#print(f"Siz uchun muzeyga kirish narxi {narx} so'm.")



#- Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
#a = float(input(f"a sonni kiriting:\n>>>"))
#b = float(input("b sonni kiriting:\n>>>"))
#if a > b : print(" a>b")
#elif a == b  : print("a=b")
#else: print ("a<b ")

#- `mahsulotlar` degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
#Yangi, `savat` degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
#Savatdagi elementlarni, `mahsulotlar` ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa `"Mahsulot do'konimizda bor"` aks holda,
#`"Mahsulot do'konimizda yo'q"` degan xabarlarni chiqaring.
mahsulotlar = ["sabzi", "karam", "olma", "piyoz", "kartoshka", "pamidor", "ko'kat", "qalampir", "bodring", "kalbasa"  ]
savat = []
print("Olishni istagan 5 ta maxsulotni kiriting:")
for k in range(5):
    savat.append(input(f"{k+1}-maxsulot:"))
for maxsulot in savat :
    if maxsulot in mahsulotlar :
        print(f"Siz tanlagan {maxsulot} maxsulot mavjud.")
    else: print(f"Siz tanlagan {maxsulot} maxsulot bizda mavjud emas")

#- Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
#Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan
# ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda 
# esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

#- `foydalanuvchilar` degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni `foydalanuvchilar` degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, `"Login band, yangi login tanlang!"` aks holda `"Xush kelibsiz, foydalanuvchi!"` xabarini chiqaring

#- Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.