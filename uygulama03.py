from random import randint

Can = 3

kelimeler = ["ronaldo", "messi", "neymar", "suarez","mbappe","modric","aguero","ribery","robben"]
kelimeSayisi = len(kelimeler)
secilen = randint(0, kelimeSayisi-1)
secilenKelime = kelimeler[secilen]
dizilenKelime = []
for diz in kelimeler[secilen]:
    dizilenKelime.append("_")
print(dizilenKelime)

while Can > 0:
    girilenHarf = input("Bakalım bu futbolcuyu bulabilecek misin? Bir harf giriniz: ")
    canKontrol = girilenHarf in secilenKelime
    if canKontrol == False:
        Can-=1
    i = 0
    for kontrol in secilenKelime:
        if secilenKelime[i] == girilenHarf:
            dizilenKelime[i] = girilenHarf
        i+=1
    print(dizilenKelime)
    print("Kalan can: "+ str(Can))

    if ("_" not in dizilenKelime) :
        print("Bildiniz...")
        break
    if Can == 0 :
        print("Bilemedinizz...")
