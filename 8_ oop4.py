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

class develper(working):
    def __init__(self,name,surname,salary,dev_language):
        #working.__init__(self,name,surname,salary) bunun yerine alt satır kullanılıyor
        super().__init__(name,surname,salary) # eğer tek sınıftan türemişse bu kalıp kullanılır
        self.dev_language=dev_language
        self.rate_incease=1.2

class manager(working):
    def __init__(self,name,surname,salary,staffs=None):
        super().__init__(name,surname,salary)
        if staffs is None:
            self.staffs=[]
        else:
            self.staffs=staffs

    def add_staff(self,staff):
        self.staffs.append(staff)
    def exit_staff(self,staff):
        self.staffs.remove(staff)

    def staff_list(self):
        for staff in self.staffs:
            print(staff.fullName())

staff1=working("ali","demir",2500)
staff2=working("kerim","bakir",2000)

dev1=develper("mehmet","dev",2350,"python")
print(dev1.dev_language)
print(dev1.fullName(),", ",dev1.salary)
dev1.increase()
print(dev1.salary)

manager1=manager("kamil","muhsir",1500,[dev1,staff1])
print(manager1.fullName())
print(manager1.staff_list())

print("\nekleme sonrası")
manager1.add_staff(staff2)
print(manager1.staff_list())
manager1.exit_staff(dev1)
print(manager1.staff_list())

# nesnenin sınıfa ait olup olmadığını kontrol etmek için
print("\nNesne o sınıfa ait mi")
print(isinstance(staff2,working))
print(isinstance(staff2,manager))

print("\n sınıflar arsında alt sınıf mı")
print(issubclass(working,manager))
print(issubclass(develper,working))
