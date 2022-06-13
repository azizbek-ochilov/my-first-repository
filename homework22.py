# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:15:00 2022

@author: hp
"""

# =============================================================================
# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
# =============================================================================

# def multiply(*sonlar):
#     """sonlarni ko'paytmasini topadi"""
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# b=multiply(1,3,4,5,6,7,8,9,23,34)
# print(b)


# =============================================================================
# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
# Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha 
# berilishi mumkin bo'lsin.
# =============================================================================
# def malumotnoma(ism, familiya, **ixtiyoriy):
#     """Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy """
#     ixtiyoriy[ism]= "ism"
#     ixtiyoriy[familiya]= "familiya"
#     return ixtiyoriy
# talaba= malumotnoma('ism',"familiya ",jinsi='erkak')