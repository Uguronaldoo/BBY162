1)
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
metin [0:21]
2)
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for x in liste :
   print(x)
3)
sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
x = input("Bir Kelime Giriniz: ")
if x == "Elma":
    print(sozluk["Elma"])
elif x == "Salatalık":
    print(x)
else:
    print("Girdiğiniz Kelime Sözlükte Bulunmamaktadır.")
