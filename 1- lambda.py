def kare(x):
    return x**2

print("normal: ",kare(8))

k=lambda x:x**3 # x in 3. kuvveti
print("lambda: ",k(2))
print(k)

deneme=lambda z,y:z*2+y**2
print("lambda2: ",deneme(3,5))

bk=lambda x,y:(x if x>y else y)
print("bk: ",bk(3,2))