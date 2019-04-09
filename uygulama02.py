print("Sınav 5 sorudan oluşmaktadır.")
print("Her soru 20 puandır.\n")
print("Başarılar Dileriz...\n")
puan=0
print("Sorular : \n")
sorular=["Soru 1 :Cristiano Ronaldo'nun forma numarası kaçtır ?",
        "Soru 2 :Şu anda Cristiano Ronaldo hangi takımda forma giymektedir ?",
        "Soru 3 :Cristiano Ronaldo hangi mevkide oynar ?",
        "Soru 4 :Cristiano Ronaldo nerelidir ?",
        "Soru 5 :Futbol kaç kişiyle oynanır ?\n"]
        
        
sıklar=["A : 7\nB : 8\nC : 9\nD : 17\n",
       "A : Juventus\nB : Barcelona\nC : Liverpool\nD : Galatasaray\n",
       "A : Kaleci\nB : Defans\nC : Ortasaha\nD : Forvet",
       "A : İspanya\nB : Yunanistan\nC : Portekiz\nD : Brezilya\n",
       "A : 9\nB : 11\nC : 10\nD : 8\n"]
       
cevaplar=["A","A","D","C","B"]
for i in range(len(sorular)):
    print(sorular[i])
    print(sıklar[i])
    cevap=input("Cevapınızı giriniz.\n")
    if cevap==cevaplar[i] or cevap==cevaplar[i].lower(): 
        print("\nDoğru cevap!\n")
        puan +=20
    else :
        print("\nYanlış cevap!\n")
   
print("Sınav Bitmiştir.")
print("Puanın : "+str(puan))