# Public, protected ve private parametreleri

class sport():
    def __init__(self,name,branch,gold,silver,bronze):
        self.name=name
        self.branch=branch
        self.mbronze=bronze # public data
        self._msilver=silver # protected data (_)
        self.__mgold=gold # private data (__)

    def  athlete_info(self):
        return "Sporcu adı: {}, branşı: {}".format(athlete1.name,athlete1.branch)

    @property
    def gold_print(self):
        medal=self.__mgold
        return "Altın madalya sayısı: {}".format(medal)

athlete1=sport("ali","100 metre",2,3,9)
print(athlete1.athlete_info())
print("Bronz madalya sayısı: ",athlete1.mbronze)
print("Gümüş madalya sayısı: ",athlete1._msilver)
#print("Altın madalya sayısı: ",athlete1.__mgold) # bu şelide olsa bile erişilmez
print(athlete1.gold_print())

# 14

