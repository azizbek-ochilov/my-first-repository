# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 17:08:59 2022

@author: hp
"""

# =============================================================================
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili
# va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# =============================================================================

# def mijoz_info(ism, familiya, t_yil, t_joy, raqam=None):
#     mijoz ={"ism":ism,
#             "familiya":familiya,
#             "t_yil": t_yil,
#             "yosh":2022-int(t_yil),
#             "t_joy":t_joy,
#             "raqam":raqam}
#     return mijoz
# print("Mijoz haqidagi ma'lumotlarni kiriting")
# mijozlar=[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     raqam = input("Raqamingiz: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, raqam))
#     javob = input("Davom erasizmi? ha/no")
#     if javob == "no":break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, {mijoz['yosh']} yoshda, telefoni: {mijoz['raqam']}")


# =============================================================================
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# =============================================================================

# #1-usul
# def kattasini_top(a,b,c):
#     """Sondan eng kattasini topadi """
#     sonlar= []
#     sonlar.append(a)
#     sonlar.append(b)
#     sonlar.append(c)
#     return max(sonlar) 
# a= kattasini_top(4, 5465, 655)
# print(a)

# #2-usul
# def kattasi(x,y,z):
#     max = x
#     if y>=max:
#         max = y
#     if z>=max:
#         max = z
#     return max
# a=kattasi(10,20,-5)
# print(a)

# =============================================================================
# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, 
# perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# =============================================================================
# def aylana(radius, pi=3.14):
#     aylana1 = {"radus":radius,
#               "diametr":radius*2,
#               "perimetr":radius*2*pi,
#               'yuza':radius**2*pi}
#     return aylana1
# aylana()


# =============================================================================
# # Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar 
# —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# =============================================================================

# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# a=tub_sonlar_top(1,56534)
# print(a)

# =============================================================================
# # Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.
#  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
#  Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# 
# =============================================================================

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))












