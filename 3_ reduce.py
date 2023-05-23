# reduce fonksiyonu liste üzerinde işlem yapar

from functools import reduce

# bir listenin en büyük elemanını bulalım
# reduce geriye bir değer göndermiyor
f=lambda a,b: a if (a>b) else b
print(reduce(f, [8,9,45,2,65,89,5,6,78]))

# faktöriyel hesaplama
fhesap=lambda x,y: x*y
print(reduce(fhesap, [1,2,3,4,5,6,7,8,9]))
print(reduce(fhesap, [x for x in range(1,10)]))

# sayısal loto kazanma ihtimali
sonuc2=reduce(lambda x,y: x*y, range(44,49))/reduce(lambda x,y:x*y, range(1,7))
print(sonuc2)