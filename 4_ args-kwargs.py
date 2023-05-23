# fonksiyona daha fazla değer gönderirsem ne olur

metin1="merhaba dünya"
metin2="python dili"
metin3="arguman alnatimi"
baslik="python programlama"

# #def metin_icerikleri(header,b,c,d):
# def metin_icerikleri(header,*args):
#     print("baslik: ",header)
#     for metin in args:
#         print(metin)
#
# metin_icerikleri(baslik,metin1,metin2,metin3,3.14,"merhaba")



# # argümana çevirerek yapalım
# def metin_icerikleri2(header,*args):
#     print(header)
#     for metin in args:
#         print(metin)
#
# metinler=[metin1,metin2,metin3]
# metin_icerikleri2(baslik,metinler) # bu şekilde metinler dizisi sadece bir argüman olarak gözükür
# metin_icerikleri2(baslik,*metinler) # bu şekilde ise diziyi böler


# kwargs argümanları anahtarlı bir şekilde alır
def metin_icerikleri3(header,**kwargs):
    print("baslik: ",header)
    for metin in kwargs.items():
        print(metin)

metin_icerikleri3(baslik,
                  metin1="merhaba dünya",
                  metin2="python dili",
                  metin3="arguman anlatimi")

