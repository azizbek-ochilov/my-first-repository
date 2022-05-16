# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:42:46 2022

@author: Azizbek Ochilov
"""

# AMALIYOT

#   VAZIFA1
#-Otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
#   (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga 
#   chiqaring: `Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan`

#otam = {"ism":"Oybek Ismoilov", "t_yil":1975, "t_oy":"oktabr", "t_kun":25, "t_joy":"Xorazm viloyati Shovot tumani" }
#print(f"Otam {otam['ism']} {otam['t_yil']}-yil {otam['t_kun']}-{otam['t_oy']} kuni {otam['t_joy']}da tavallud topganlar. ")


#VAZIFA2
#- Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: `Alining sevimli taomi osh`

#taom = {"Ali": "osh", "Vali ":"shashklik", "Lazizbek":"makaron", "Azizbek":"dimlama", "Madina": "manti"}
#print(f"Ali {taom['Ali']}ni yoqtiradi.\nVali {taom['Vali ']}ni yoqtiradi.\nLazizbek esa  {taom['Lazizbek']}ni yoqtiradi.")



#VAZIFA3
#- Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
#python_izohli_lugati = {"float":"matinni son ko'rinshida oladi", "integer":"matinni butun son ko'rinishiad qabul qiladi", "string":"matn", "if":"agar",
#          "else":"yo'qsa", "elif":"mabodo", "title":"bosh xarf", "upper":"katta harf", "reverse":"teskari","for in":"ichida", "and":"va" }

#VAZIFA4
#- Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
#Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
#a = input("pytonda qiynalayotga alamangizni kiriting\n.>>>").lower()
#print(python.get(a,"Bunday so'z mavjud emas"))


#VAZIFA5
#- Yuqoridagi vazifani `if-else` yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring. 
 
python_izohli_lugati = {"float":"matinni son ko'rinshida oladi", "integer":"matinni butun son ko'rinishiad qabul qiladi", "string":"matn", "if":"agar",
          "else":"yo'qsa", "elif":"mabodo", "title":"bosh xarf", "upper":"katta harf", "reverse":"teskari","for in":"ichida", "and":"va" }
kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")





