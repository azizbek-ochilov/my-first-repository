# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:26:46 2022

@author: hp
"""

print("Assalomu alaykum bankimizga hush kelibsiz")
savol1= input("Kerakli tilni tanlang:\nO'zbek tilini tanlash uchun 1 ni yuboring")
n=4
kod = ('1234')
while n!=0:
    savol2 =input("Pin kod ni kiriting:")
    if savol2==kod :
        keyingi_bosqich = True
        print("Parol to'ri")
        break
    else: 
        print("Pin kod xato")
        print(f"{n-1} ta urunish qoldi")
        if len(savol2) != 4: 
            print("Pin kod 4 xonadan iborat bo'ladi")
            keyingi_bosqich = "xato"
    n-=1
while True :    
    if keyingi_bosqich == True:
        balans = 1000000
        print("\n1.Naqd pul yechish\n2.Balansni ko'rish\n3.Parolni o'zgartirish\n4.Sms xabarnoma hizmatini yoqish\n5.Dasturni yakunlash")
        savol3 = input("Bajarishni istagan amaliyotni tartib raqamini jo'nating:\n>>>")
        if int(savol3) not in range(1,6) :
            print("Iltimos (1,5) oraliqda son kiriting. ")
        if savol3 =="1":
            print("Yechishni istagan summani tartib raqamini yuboing:")
            savol4=input("1.50000 so'm\n2.100000 so'm\n3.300000 so'm\n4.500000 so'm \n5.Boshqa summa\n>>>")
            if savol4 == "1" :
                print("Pul tayyorlanmoqda...")
                print(f"Amaliyot bajatildi. Kartangizda mavjud mablag' {balans-50000}")
                balans = balans-50000 
            if savol4 == "2" :
                print("Pul tayyorlanmoqda...")
                print(f"Amaliyot bajatildi. Kartangizda mavjud mablag' {balans-100000}")
                balans = balans-100000
            if savol4 == "3" :
                print("Pul tayyorlanmoqda...")
                print(f"Amaliyot bajatildi. Kartangizda mavjud mablag' {balans-300000}")
                balans = balans-300000
            if savol4 == '4' :
                print("Pul tayyorlanmoqda...")
                print(f"Amaliyot bajatildi. Kartangizda mavjud mablag' {balans-500000}")
                balans = balans-500000
            if savol4 == "5" :
                summa = input(f"Summani kiriting: ")
                summa = int(summa)
                if summa > 1000000: print("Hisobingizda yetarli mablag' mavjud emas")
                else:
                    print("Pul tayyorlanmoqda...")
                    print(f"Amaliyot bajatildi. Kartangizda mavjud mablag' {balans-summa}")
        if savol3 == "2":
            print(f"Sizning balans {balans}")
        if savol3 == "3":
            yangi_p = input("Yangi parol \n>>>")
            tasdiq = input ("Parolni tasdiqlang:\n>>>")
            if yangi_p == tasdiq:
                kod = yangi_p
                print("Parolingiz muvofaqqiyatli o'zgartirildi")
            else: print("Parollaringiz bir birini tasdiqlamadi")
        if savol3 == "4":
            while True:
                raqam = input("Raqaminizni kiriting(misol:998xxxxxxxxx)\n>>>")
                if len(raqam) == 12:
                    print("Amaliyot muvoffaqiyatli bajarildi")
                    break
        if savol3 == "5":
            print("Dastur o'z ishini tamomladi") 
            break
        
else:        
    print("Dastur ishi yakullandi. Kartangiz bizda qoladi😴")

        
        
        
        
        