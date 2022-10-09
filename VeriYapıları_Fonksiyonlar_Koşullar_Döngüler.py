################################################################################################
#                                   PYTHON ALIŞTIRMALAR                                         #
#################################################################################################
import pandas as pd

#region  1

x = 8
type(x)
y = 3.2
z = 8j + 18
a = 'Hello World'
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}

t = {"Machine Learning", "Data Sciemce"}

s = {"Python", "Machine Learning", "Data Science"}


type(x)
type(y)
type(z)
type(l)
type(a)
type(b)
type(c)
type(d)
type(t)
type(s)

#region Listeler
## Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

#endregion

#region Sözlükler
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak
#endregion

#region Tupple
# Değiştirilemez
# Kapsayıcı
# Sıralı
#endregion

#region Kümeler
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı
#endregion

#endregion


#region  2
text = "The goal is to turn data into information, and information into insight."

text.upper().replace(",", "").replace(".", "").split()

#endregion

#region  3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

#Adım1: Verilen listenin eleman sayısına bakınız.
len(lst)

#Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0]

lst[10]

#Adım3: Verilen iste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
data_lst = lst[0:4]

#Adım4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)

#Adım5: Yeni bir eleman ekleyiniz
lst.append(99)

#Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz.
lst.insert(8, 'N')
#endregion


#region  4
#Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christan': ['America', 18],
        'Daisy': ['England', 12],
        'Antonio': ['Spain', 22],
        'Dante': ['Italy', 25]}


#Adım1: Key değerlerine erişiniz.
dict.keys()


#Adım2: Value'lara erişiniz.
dict.values()


#Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict.update({'Daisy': ['England', 13]})

#Adım4: Key değeri Ahmet value değeri[Turkey,24] olan yeni bir değer ekleyiniz.
dict.update({'Ahmet' : ['Turkey', 24]})

#Adım5: Antonio'yu dictionary'den siliniz.
dict.pop('Antonio')
#endregion

#region  5

#Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]


def func_tek_cift(list_):
    tek = list()
    cift = list()
    for i in list_:
        if i % 2 == 0:
            cift.append(i)
        else:
            tek.append(i)
    return cift, tek


cift_degerler, tek_degerler = func_tek_cift(l)
print(cift_degerler, tek_degerler)

#endregion


#region  6

#Aşağıda verilen listede mühendislik ve tıpfakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ['Ali', 'Veli', 'Ayşe', 'Talat', 'Zeynep', 'Ece']

for index, val in enumerate(ogrenciler, 1):
    if index <= 3:
        print('Mühendislik Fakültesi ', index, '.', val)
    else:
        print('Tıp Fakültesi', index-3, '.', val)

#endregion


#region  7
#Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ['CMP1005', 'PSY1001', 'HUK1005', 'SEN2204'] ; kredi = [3, 4, 2, 4] ;  kontenjan = [30, 75, 150, 25]

for ders_kodu, kredi, kontenjan in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontejanı {kontenjan} kişidir.")

#endregion


#region  8

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))

kume(kume1, kume2)
#endregion
import pandas as pd
ogrenciler = ['Ali', 'Veli', 'Ayşe', 'Talat', 'Zeynep', 'Ece']

def ogrenciler_fun(l):
    A = list()
    B = list()
    for index, row in enumerate(l):
        if index < 3:
           muhendislik_fak = "mühedislik fakültesinde " + str(index + 1) + " olan öğrenci " + row
           A.append(muhendislik_fak)
           #muhendislik = muhendislik_fak.split('\n')
           print("mühedislik fakültesinde " + str(index + 1) + " olan öğrenci " + row, sep='\n' )

        else:
           tıp_fakultesi = "tıp fakültesinde " + str(index - 2) + " olan öğrenci " + row
           B.append(tıp_fakultesi)
           #tip = tıp_fakultesi.split('\n')
           print("tıp fakültesinde " + str(index - 2) + " olan öğrenci " + row, sep='\n')
    return A, B
muhendislik, tıp = ogrenciler_fun(ogrenciler)

df = pd.DataFrame(muhendislik, tıp)

##pd.concat(muhendislik, tıp)


