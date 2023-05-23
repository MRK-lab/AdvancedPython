# macih methots

class working():
    rate_incease=1.05
    number_staff=0

    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        self.email=self.name+self.surname+"@company.com"
        working.number_staff=working.number_staff+1

    def fullName(self):
        return "name: {}, surname: {}".format(self.name,self.surname)
    def increase(self):
        self.salary=(self.salary*self.rate_incease)

    def __str__(self): # <__main__.working object at 0x0000018458C8C390> bu şekilde yazdırmamak için
        return "{}, {}".format(self.fullName(),self.email)

    def __repr__(self): # str olmadığı durumlarda kullanılır. önce __str__ çalışıyor. ya da özel çağrılabiliyor staff.__ gibi
        return "calisan ('{}','{}','{}')".format(self.name,self.surname,self.salary)

    def __add__(self, other):
        return self.salary+other.salary


staff1=working("ali","demir",2500)
staff2=working("kerim","bakir",2000)


print(staff1)
print(staff2.__repr__())
print(repr(staff1))
print(str(staff1))

print("\n\n")
print(staff1+staff2) # def __add__ işlemi



