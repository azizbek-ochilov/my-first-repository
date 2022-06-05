# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 21:44:36 2022

@author: hp
"""

# ism = input("Assalomu alaykum ismingiz nima? ")
# savol = input(f"Nimagaplar {ism.title()}. Yoshingiz nechida?")
# print(f"men ham {savol} yoshdaman.")


# # 10000 gacha bo'lgan toq sonlarni sanaydigan sodda dastur
# son = 1 # son ga 1 qiymatini beramiz
# while son<=10000: # toki son 10000 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son += 2 # songa 1 qo'shamiz.son+2

# =============================================================================
# Kiritilgan sonni kvadratini hisoblovchi dastur tuzish usullari (A,B va C)
# =============================================================================


## A variant

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

## B variant 

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)

## C variant 

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
    


# =============================================================================
# # =============================================================================
# # # AMALIYOT
# # 
# # 1. Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# # Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# # 
# # 2. Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
# #     7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
# #     Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
# #     Foydalanuvchi `exit` yoki `quit` deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# #     - Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
# #     
# # 3. Quyidagi dasturda bir nechta mantiqiy xatolar bor.
# #  Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# 
# while True:
#     qiymat = input(savol)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
# # =============================================================================
# =============================================================================


# #1 
# b = []
# a = (" Yoqtirgan kitoblaringzini kiriting(dasturni to'xtatish uchun 'quit' ni yuboring): ")
# while True: 
#     qiymat = input(a)
#     if qiymat == "quit":
#         break 
# print(f"Sizning yoqtirgan kitoblaringiz juda ajoyib. ")


# #2
# a = "Muzey malumotlarini bilish uchun yoshni kiriting:"
# a += "(dasturni tugatuvchi sehirli so'z 'stop')"
# while True:
#         qiymat = input(a)
#         if qiymat == "quit" or qiymat == "stop": 
#             break 
#         yosh = int(qiymat)
        
#         if yosh < 7: 
#             narx = 2000
#         elif 7<= yosh <18: 
#              narh = 3000
#         elif 18< yosh>=  65 : narh= 10000  
#         else: narx=0
        
#         if narh==0:
#             print("Sizga chipta bepul")
#         else:
#                 print(f"Chipta {narh} so'm")

# #3
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     a = input(savol)
#     qiymat = int(a)
#     if qiymat<0:
#         continue
#     elif qiymat=='Exit':
#         break
#     else:
#         ildiz = float(qiymat)**(0.5)
#     print(f"{qiymat} ning ildizi {ildiz} ga teng")
    