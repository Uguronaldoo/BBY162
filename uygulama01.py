print("Sınav 5 sorudan oluşmaktadır.")
print("Her soru 20 puandır.\n")
print("Başarılar Dileriz...")
puan=0
#1.Soru
print("Cristiano Ronaldo'nun forma numarası kaçtır ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="7":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
	
#2.Soru

print("Şu anda Cristiano Ronaldo hangi takımda forma giymektedir ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="Juventus" or cevap=="juventus" or cevap=="Juve" or cevap=="juve":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")

#3.soru


print("Cristiano Ronaldo hangi mevkide oynar ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="forvet" or cevap==":Forvet":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
	
	
#4.Soru

print("Cristiano Ronaldo nerelidir ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="Portekiz" or cevap=="portekiz":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
	
#5.Soru

print("Futbol kaç kişiyle oynanır ?\n")
print("Cevabınızı giriniz : \n")
cevap=input()
if cevap=="11":
	puan =puan+20
	print("\nTebrikler! Cevabınız doğru.")
	print("Mevcut puanınız: "+ " " + str(puan)+"\n")
else:
	print("Cevabınız yanlış.")
	print("Bu sorudan hiç puan alamadınız.")
	print("Mevcut puanınız "+" "+str(puan)+"\n")
print("Sınav bitmiştir .")	
