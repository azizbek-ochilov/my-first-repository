# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 22:28:46 2022

@author: hp
"""

#VAZIFALAR

# =============================================================================
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# =============================================================================

# print("Qani nimalar keldi bugun?")
# mahsulotlar = []
# n=1 
# while True:
#     mahsulot = input(f"{n}-mahsulot:")
#     savol = input(f"Yana bormi maxshulot? Tugagan bo'sa \"yo'q\" deng, bor bo'lsa \"ha\".")
#     mahsulotlar.append(mahsulot)
#     if savol == "yo'q": 
#         break ;
#     else: n+=1
# print("Siz tomoningizdan bugun shu mahsulotlar keldi:")
# print(mahsulotlar)


# =============================================================================
# E-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# =============================================================================


# savdo ={}
# n=1
# while True:
#     savol = input(f"{n}-mahsulot: ")
#     narh = input(f"{savol.title()} narhini kiriting: ")
#     savol2 = input(f"Agar yana savatga mahsulotlar kiritishni hohlasangiz 'enter'ni bosing")
#     savdo[savol] = int(narh)
#     if savol2 == "":
#         n += 1
#     else: break
# for savol , narh in savdo.items():
#     print(f"Bizda mavjud bo'gan {savol}ning narhi {narh}ga teng.")
    

# =============================================================================
# Yuqoridagi ikki dasturni jamlaymiz.
#   Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
#   (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
#   aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# =============================================================================

    
# print("Harid qilishini hohlagan mahsulotlaringizni kiriting va biz uni bizda mavjud tovarlar bilan solishtiramiz")  
# bor= {"olma":12000, "ko'kat":5000, "shaftoli":15000, "nok":23000, "qovun":30000, "anor":23000, "tarvuz":25000, "muzqaymoq":5000}    
# mahsulotlar = ["olma", "anor"]
# # n=1 
# # while True:
# #     mahsulot = input(f"{n}-mahsulot:")
# #     savol = input(f"Yana bormi maxshulot? Tugagan bo'sa \"yo'q\" deng, bor bo'lsa \"ha\".")
# #     mahsulotlar.append(mahsulot)
# #     if savol == "yo'q": 
# #         break ;
# #     else: n+=1   
# while mahsulotlar : 
#     tovar = mahsulotlar.pop
#     if tovar in bor.keys():
#         narh = bor[tovar]
#         print(f"{tovar} bizda mavjud va bahosi {narh}");
#     else: print(f" {tovar} bizda mavjudmas")
    

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
    
    
    
    
    
    
    
    
