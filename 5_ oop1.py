class calisan:

    katsayi=5

    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        self.eposta=self.ad+self.soyad+"@sirket.com"

    def tamad(self):
        return "adi: {}, soyadı: {}".format(self.ad,self.soyad)

personel1=calisan("ali","demir",2500)

# personel1.ad="ali"
# personel1.soyad="demir"
# personel1.maas=2500

personel2=calisan("kerim","kerim",1950)
# personel2.ad="kerim"
# personel2.soyad="bakir"
# personel2.maas=1950

# print(personel1)
# print(personel1.ad,personel1.soyad,personel1.eposta)
# print(personel1.tamad())
#
# print(personel2)
# print(personel2.ad,personel2.soyad)
# print(personel2.tamad())
# print(personel2.eposta)

print(calisan.tamad(personel2))
print(calisan.katsayi)



