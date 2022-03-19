# Python-Note-Practice

## Dosya Okuma Yazma

Pythonda text dosyasını okuma için, Bu adımları Takip edin:

1-)İlk olarak, open() fonksiyonu kullanarak okumak için text dosyasını açın.
2-)İkinci olarak read(), readline() yada readlines() methodunu kullanarak text dosyasının
içindeki metinleri oku.
3-)Son olarak, close() methodunu kullanarak dosyayı kapatın.

### 1) open() function
open() fonksiyonu 2 tane parametre almaktadır.Bunlar dosyanın_yolu ve mod
dosya_yolu: text dosyasının bulundugu dosyanın yolunu göstermektedir.
Python kodunuz ile text dosyası aynı klasör içinde ise sadece text dosyasının adını girmeniz yeterlidir.

mod: dosyayı açarken hangi mod'da açmak istediğinizi belirten parametredir.
'r' : Text dosyasını okumak için açar.
'w' : Text dosyasını yazman için açar.
'a' : Text dosyasını ekleme yapmak için açar.

Kullanışı = open(dosya_yolu, mod)
f = open('file.txt','r')

### 2) Dosyayı Okuma

Bir text dosyasından metin okuyabilmek için 3 method kullanılır.Bunlar:
  *read() - Bir dosya'ya girilen tüm stringleri okur.
  *readline() - Text dosyasındaki tüm string satırları değerlerini satır - satır okur.
  *readlines() - Text dosyasının bütün satılarını okur ve string listesi şeklinde dönderir.
 
 ### 3) close() methodu
 
 Bu method açılan text dosyasının kapatılmasını sağlar.
 Dosyayı kapatmak neden önemlidir.Çünkü dosya kapatılmazsa program crashlenebilir yada
 dosya bozulabilir.

f.close()

Dosyayı otomatik bir şekilde kapatmak için close() methodu yerine aşşağıdaki gibi with ifadesi kullanılır.
  with open(dosya_yolu) as f:
      contents = f.readlines()
