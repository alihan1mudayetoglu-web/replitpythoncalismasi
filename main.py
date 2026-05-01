# değişkenler sayısal veya metinsel değerlerin bilgisayara
# kayıt edilmesi için kullanılır.

# kullanıcıdan metinsel değerleri input() ile alınır
# kullanıcıdan sayısal değerleri int(input()) ile alınır 
sinif = "kırmızı"
if sinif == "kırmızı" :
  print("youtube")
  print("koşulun içinde bir tab boşlık bırakılır")
else:
  print("youtube sınıfında değilsiniz")



ad = input("lütfen isminizi giriniz:")
şifre = input("lütfen şifrenizi giriniz:")
# kullanıcıdan aldınğınız isim değeri sisin isinize eşit ise
# selamlar youtube hoşgeldin, ad
# ad yanlış ise yanlış sınıftasınız uyarısını yazdırın
if ad == "Deniz" :
   print("hoş geldin yaman bey.")
  
else:
   print("yok giremezsin aga.")
  
if şifre == "456" :
 print("hoş geldin yaman bey.")

else:
 print("yok giremezsin aga.")
import random

a = random.randint(1,100)
b = random.randint(1,200)
print(a, "+", b," = toplamının sonucu ")
cevap = int(input("işleminin sonucu: "))
if cevap == a + b :
  print("doğru cevap")

else:
  print("yanlış cevap doğru cevap: ", a+b)
  cevap = random.randint(1,31)
  a = random.randint(1,31)
  cevap = int(input("tahmin ediniz:"))
if cevap == a:
  print("doğru tahmin")

else:
  print("yanlış tahmin",a)
