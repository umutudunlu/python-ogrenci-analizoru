
isim =input("adiniz ve soyadinizi giriniz :")
isim = isim.title()
liste =[]
for i in range(3):
 not_girisi = int(input(f"{i +1}.notunuzu giriniz :"))
 liste.append(not_girisi)
ortalama =round(sum(liste)/ len (liste),2)
if ortalama %2 == 0:
   print (f"(ortalama ({ortalama})bir çift sayidir)")
else:
   print(f"(ortalama ({ortalama})bir tek sayidir)")
if ortalama >= 85:
   durum = "tebrikler,pek iyi"
elif ortalama >= 50:
   durum= "basarali , geçti"
else :
    durum ="üzgünüm ,kaldiniz"
print(durum)
ogrenci = {
    "isim" : isim,
    "notlar" : liste,
    "ortalama": ortalama,
    "durum" : durum,
}
for anahtar, deger  in ogrenci.items():
   print(f"{anahtar}: {deger}")