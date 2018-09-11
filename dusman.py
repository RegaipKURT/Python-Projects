import random

class dusman:

    def __init__(self, isim = "Düşman", can = 100, guc = 10, mermi = 40):
        self.isim = isim
        self.can = can
        self.guc = guc
        self.mermi = mermi

    def yazdir(self):
        print("İsim:",self.isim, "Can:",self.can, "Güç:",self.guc, "Mermi:",self.mermi)
        print ("---------------------------------")

    def saldir(self):
        print(self.isim + "saldırıyor...")
        harcanan_mermi = random.randrange(0,40)
        print (str(harcanan_mermi + " mermi harcandı..."))
        self.can -= 10
        self.guc -= 10
        self.mermi -= harcanan_mermi
        return (harcanan_mermi,self.guc)

    def savun(self, harcanan_mermi, guc):
        print("Vuruldumm....")
        self.can -= (harcanan_mermi * guc)

    def mermi_bitti_mi(self):
        if (self.mermi <= 0):
            print(self.isim + ": mermi bitti...")
        return True

    def hayatta_mi(self):
        if (self.can <= 0):
            print("Ölüyorummm.....")


dusmanlar = []

i = 0
while(i < 10):
    rastgelecan = random.randrange(50,100)
    rastgelemermi = random.randrange(80, 160)
    rastgeleguc = random.randrange(70,100)
    yenidusman = dusman("Düşman" + str(i+1), rastgelecan, rastgeleguc,rastgelemermi)
    dusmanlar.append(yenidusman)
    i += 1

for dusman in dusmanlar:
    dusman.yazdir()

i = 0
while (i < 0):
    randomdusman1 = random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)
    donendeger = dusmanlar(randomdusman1).saldir()
    dusmanlar(randomdusman2).savun(donendeger[0],donendeger[1])
    dusmanlar(randomdusman1).yazdir()
    dusmanlar(randomdusman2).yazdir()
    print("Round Bitti...")
    i += 1
