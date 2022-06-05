# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:14:54 2022

@author: hp
"""

# =============================================================================
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# =============================================================================

musk = {"ism":"elon musk", 
              "yosh":"48", 
              "kasb":"progromer"}
azizbek = {"ism": "azizbek ochilov",
            "yosh":17,
            "kasb":"talaba"}
bill_gates = {"ism": "bill gates",
              "yosh":70,
              "kasb":"ixtirochi"}
ferrari = {"ism": "enzo ferrari",
            "yosh":"99+",
            "kasb":"ferrari egasi"}
mashxurlar = [ musk , azizbek , bill_gates , ferrari]
for shaxs in mashxurlar:
    ism = shaxs["ism"]
    yosh = shaxs["yosh"]
    kasb = shaxs["kasb"]
    print(f"{ism.title()} {yosh} yoshda. Kasbi {kasb}")

# =============================================================================
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# =============================================================================
 
# musk = {"ism":"elon musk", 
#               "yosh":"48", 
#               "kasb":"progromer",
#               "asar":["Elon Musk", "Secrets of being billionare"]}
# azizbek = {"ism":"azizbek ochilov",
#             "yosh":'17',
#             "kasb":"talaba",
#             "asar":["Hayotiy tajribalarim", "Omad va Muvaffaqqiyat"]}
# bill_gates = {"ism": "bill gates",
#               "yosh":70,
#               "kasb":"ixtirochi",
#               "asar":["The Road Ahead", "Bill Gares Quotes"]}
# ferrari = {"ism": "enzo ferrari",
#             "yosh":"99+",
#             "kasb":"ferrari egasi",
#             "asar":["The car", "The man"]}
# mashxurlar = [ musk , azizbek , bill_gates , ferrari]
# for shaxs in mashxurlar:
#     ism = shaxs["ism"]
#     yosh = shaxs["yosh"]
#     kasb = shaxs["kasb"]
#     asar = shaxs["asar"]
#     print(f"{ism.title()}ning kitoblari:")
#     for a in asar: print(a)

# =============================================================================
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
#     uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
# =============================================================================
 
# kinolar = {"Lazizbek":["Terminator", "Kalmar o'yini", "Samolardan balandda"],
#            "Ro'zimboy":["Abdullajon", "Qasoskorlar", "Shamollarda qolgan hislarim" ],
#            "Husanboy":["Tinchlik", "spyder men ", "Islomxo'ja"]}
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)


# =============================================================================
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
# =============================================================================

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }
# for davlat, info in davlatlar.items(): 
#     if davlat.lower()=="aqsh": davlat = davlat.upper()
#     else: davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")



