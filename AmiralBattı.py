from random import seed
from random import randint
seed(1)
listOyun = []
listGizliOyun = []
boyut = 12
boyut = int(input("Harita boyutu seçiniz (Tercihen 3 ün katları): "))#Harita boyutunu kullanıcıya seçtiriyoruz.
listGemi = []
class Gemi:
  def __init__(self, x1, y1, x2, y2):
    self.x1 = int(x1)
    self.y1 = int(y1)
    self.x2 = int(x2)
    self.y2 = int(y2)
    self.parca = x2 - x1 + y2 - y1 + 1

def gemiyiVur(x, y):
    for i in range(0, len(listGemi)):
        if(listGemi[i].x1 <= x and listGemi[i].x2 >= x and listGemi[i].y1 <= y and listGemi[i].y2 >= y):
            listGemi[i].parca -= 1
            if listGemi[i].parca == 0:
                print("\n\nGemi ", i+1, " Yokedildi !\n")

def gemiOlustur(i, j):# rasgele bir boyutta gemi oluşturma
    kontrol = True
    while kontrol:
        degisken1 = randint(1, 4)
        degisken2 = randint(1, 2)#sağdan sola veya yukarıdan aşşağı rasgele
        if(degisken2 == 1 and boyut - j > degisken1):
            kontrol = False
            for en in range(j, j + degisken1 - 1):
                if not listOyun[i][en] == '*':
                    kontrol = True#gemi yeri uygun mu?
        if(degisken2 == 2 and boyut - i > degisken1):
            kontrol = False
            for boy in range(i, i + degisken1 - 1):
                if not listOyun[boy][j] == '*':
                    kontrol = True
    if(degisken2 == 1):
        listGemi.append(Gemi(j, i, j + degisken1 - 1, i))
        for en in range(j, j + degisken1):
            listOyun[i][en] = 'x'
    if(degisken2 == 2):
        listGemi.append(Gemi(j, i, j, i + degisken1 - 1))
        for boy in range(i, i + degisken1):
            listOyun[boy][j] = 'x'


for i in range(0, boyut):
    listOyun.append([])
for i in range(0, boyut):
    listGizliOyun.append([])
for i in range(0, boyut):
    j = 0
    for j in range(0, boyut):
        listOyun[i].append('*')
for i in range(0, boyut):
    j = 0
    for j in range(0, boyut):
        listGizliOyun[i].append('?')
for i in range(0, boyut):
    j = 0
    for j in range(0, boyut):
        if listOyun[i][j] == '*':
            degisken = randint(0, 7)
            if degisken == 1:
                   gemiOlustur(i, j)
print("\n---------------------------------------\n")
mod = int(input("1 - Gizli Mod\n2 - Açık Mod\n\n\tBir Mod Seçiniz (1 veya 2): "))
print("\n")
hak = int(boyut * boyut / 3)
kazanmaDurumu = False
toplamGemiParcası = 0
for i in range(0,len(listGemi)):
    toplamGemiParcası += listGemi[i].parca
while hak > 0:
    if(mod == 2):
        for i in range(0, boyut):
            j = 0
            for j in range(0, boyut):
                print(listOyun[i][j], end = '')
            print()
    elif(mod == 1):
        for i in range(0, boyut):
            j = 0
            for j in range(0, boyut):
                print(listGizliOyun[i][j], end = '')
            print()
    x, y = input("\nBir koordinat seçiniz.(Uygun format : x y): ").split()
    x = int(x)
    y = int(y)
    print(60*'\n')
    if(listOyun[y][x] == '*'):
        if(listGizliOyun[y][x] == '*'):
            print("\nBu Noktayı Daha önce Vurdunuz !\n")
        else:
            print("\nBoş bir Noktayı Vurdunuz !\n")
            listGizliOyun[y][x] = '*'
            hak -= 1
    else:
        if(listGizliOyun[y][x] == 'x'):
            print("\nBu Noktayı Daha önce Vurdunuz !\n")
        else:
            print("\nBir Gemiyi Vurdunuz !\n")
            listGizliOyun[y][x] = 'x'
            gemiyiVur(x, y)
            hak -= 1
            toplamGemiParcası -= 1
            if(toplamGemiParcası == 0):#Tüm parçalar yok edilince kazanır.
                kazanmaDurumu = True
                break
    print("\nKalan hak: ", hak, "\n")
    print("\nKalan Gemi Parcası : ", toplamGemiParcası, "\n")

if(kazanmaDurumu):
    print("\n\n\t\tTebrikler Kazandınız !!!\n\t\tSkorunuz : ", hak)
else:
    print("\n\n\t\tMalesef Kaynettiniz !!!")
            
#for i in range(0, len(listGemi)):
#    print(i + 1, ". Gemi: (", listGemi[i].x1, ", ", listGemi[i].y1, ")", " - (", listGemi[i].x2, ", ", listGemi[i].y2, ")  Parça : ", listGemi[i].parca)


















    
