# getter, setter, deltter
# get: bilgileri al
# set: bilgileri düzenle
# del: bilgileri sil

class working:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    @property
    def email(self):
        self.emaill = self.name + self.surname + "@company.com"
        return self.emaill

    @property
    def fullName(self):
        return "adı: {}, soyadı: {}".format(self.name,self.surname)

    @fullName.setter
    def fullName(self,come_name):
        name,surname=come_name.split(" ")
        self.name=name
        self.surname=surname

    @fullName.deleter
    def fullName(self):
        self.name=None
        self.surname=None
        print("User information deleted...")

staff1=working("ali","demir")
print(staff1.name)
print(staff1.email)
print(staff1.fullName)
# staff1.name="can" # isim değiştiriyoruz burada ama biz tam ad değiştirmek istiyoruz

staff1.fullName="can bakir"

print("\nDeğiştirdikten sonra")
print(staff1.name)
print(staff1.email)
print(staff1.fullName)

print("\nkullanıcı silme")
del staff1.fullName

print(staff1.name)
print(staff1.email)
print(staff1.fullName)

