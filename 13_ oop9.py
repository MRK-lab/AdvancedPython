# Muti inheritance _ Çoklu kalıtım

class footballer():
    run="koşabilir"
    sprint="depar at"
    salary=500
    def __init__(self,ayak="sağ"):
        self.mevki="orta"
        self.ayak = ayak


class basketball():
    tourniquet="turnike atabilir"
    three="üçlük atabilir"
    salary=750
    def __init__(self):
        self.area="ileri"


class multi_sport(basketball,footballer): # baskın karakter ilk yazılandır
    def __init__(self,ayak):
        basketball.__init__(self)
        footballer.__init__(self,ayak)


mahmut=multi_sport("sol")

print(mahmut.tourniquet)
print(mahmut.run)
print(mahmut.salary)
print(mahmut.area)
print(mahmut.mevki)
print(mahmut.ayak)


