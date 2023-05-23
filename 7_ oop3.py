class working:

    rate_increase=1.05
    number_staff=0

    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        self.email=self.name+self.surname+"@compant.com"
        working.number_staff=working.number_staff+1
    def fullName(self):
        return "name: {}, surname: {}".format(self.name,self.surname)
    def increase(self):
        self.salary=(self.salary*self.rate_increase)

    @classmethod # sınıfın kendisini etkiliyor
    def rate_increase_change(cls,new_rate):
        cls.rate_increase=new_rate

    @classmethod
    def new_staff(cls,staff_info):
        name, surname, salary = staff_info.split("-")
        return cls(name,surname,salary)

    @staticmethod # statik methot kullanımında fonksiyonda cls yazmasına gerek yoktur
    def phone_no(phone): # sınıfa müdahale etmez geriye değer gönderir
        return phone.split(" ")


staff1=working("ali","demir",2500)
staff2=working("veli","bakir",1500)

mstuff1="veli-can-4000"
mstuff2="mert-haydar-3500"

new_stuff1=working.new_staff(mstuff1)
new_stuff2=working.new_staff(mstuff2)

print(new_stuff1.fullName())
print(new_stuff2.fullName())

phone_number="0123 456 78 90"
print(working.phone_no(phone_number))

# name, surname, salary=mstuff1.split("-")
# new_staff=working(name,surname,salary)
# print(new_staff.fullName(),", ",new_staff.email)



#working.rate_increase_change(2)

# print(staff1.salary)
#staff1.increase()
#print(staff1.salary)
#
# staff2.rate_increase=2
# staff2.increase()
# print(staff2.salary)


