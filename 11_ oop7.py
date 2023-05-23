# namespace, scope, local, global, nonlocal

# # kimlik bilgileri sabittir
# a=2
# print("id(2)",id(2))
# print("id(a)",id(a))



# a=2
# print("id(a)",id(a))
# a=a+1
# print("id(a)",id(a))
# print("id(3)",id(3))
# b=2
# print("id(b)",id(b))



# def printHello():
#     print("Hello")
# a=printHello()
# print(id(a))



# def dis_fonk():
#     b=20
#     def ic_fonk():
#         c=30
# a=10
# print(a,b,c) # a yazar b ve c tanımlı değil der



# def dis_fonk():
#     a=20
#     def ic_fonk():
#         a=30
#         print("a: ",a)
#     ic_fonk()
#     print("a: ",a)
# a=10
# dis_fonk()
# print("a: ",a)



# def dis():
#     global a
#     print(a)
#     a=20
#     print(a)
#     def ic():
#         global a
#         a=30
#         print("a: ",a)
#     ic()
#     print("a: ",a)
# a=10
# dis()
# print("a: ",a)



def scope_test():
    def do_local():
        spam="local spam"

    def do_nonlocal():
        nonlocal spam
        spam="nonlocal spam"

    def do_global():
        global spam
        spam="global spam"

    spam="test spam"
    do_local()
    print("After local assigment: ",spam)
    do_nonlocal()
    print("After nonlocal assigment: ",spam)
    do_global()
    print("After global assigment: ", spam)

scope_test()
print("In global scope", spam)


