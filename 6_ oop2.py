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

staff1=working("ali","demir",2500)
print(working.number_staff)
staff2=working("veli","bakir",1500)
print(working.number_staff)

print(staff1.salary)
staff1.increase()
print(staff1.salary)

print(staff2.salary)
staff2.rate_increase=2
staff2.increase()
print(staff2.salary)

