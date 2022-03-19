def ortalamalari_oku():
    with open('new_file.txt','r',encoding='utf-8')as file:
        line = file.readline()
        while line:
            print(notlari_oku(line))
            line = file.readline()
            
            
def notlari_oku(line):
    line = line[:-1]
    liste = line.split(',')
    
    ogrenci_adi = liste[0]
    not1 = int(liste[1])
    not2 = int(liste[2])
    not3 = int(liste[3])

    ortalama = (not1 + not2 + not3) / 3
    
    if ortalama > 90:
        harf = "AA"
    elif ortalama > 85:
        harf = "BA"
    elif ortalama > 80:
        harf = "BB"
    elif ortalama > 75:
        harf = "CB"
    elif ortalama > 70:
        harf = "CC"
    elif ortalama > 65:
        harf = "DC"
    elif ortalama > 60:
        harf = "DD"
    elif ortalama > 50:
        harf = "FD"
    else:
        harf = "FF"
        
    return f"{ogrenci_adi}: {harf}\n"

def not_gir():
    isim = input("Ogrenci Adi: ")
    not1 = input("not 1: ")
    not2 = input("not 2: ")
    not3 = input("not 3: ")
    with open('new_file.txt','a',encoding='utf-8')as file:
        file.write(f"{isim},{not1},{not2},{not3}")
        

def notlari_kaydet():
    with open('new_file.txt','r',encoding='utf-8')as file:
        liste = []
        for eleman in file:
            ortalama=notlari_oku(eleman)
            liste.append(ortalama) 
            print(liste)
        with open('new_file2.txt','w',encoding='utf-8')as file2:
            for ele in liste:    
                file2.write(ele)

while True:
    islem = input('1- Notlari Oku\n2- Not Gir\n3- Notlari Kayit Et\n4- Cikis\n')
    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        notlari_kaydet()
    elif islem == "4":
        break
    else:
        print("Dogru sayi girdiginizden emin oldunuz")