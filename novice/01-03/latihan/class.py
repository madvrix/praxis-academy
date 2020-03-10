#base
# class pertama:
#     #init selalu di run otimatis setiap class di panggil
#     def __init__(self):
#         print('telah di run otomatis')
#     def tampil(self):
#         print("memanggil fungsi tampil a")
#     def tampil2(self):
#         print('memanggil fungsi tampil b')

# # a=pertama()
# # a.tampil()
# pertama().tampil()
# pertama().tampil2()

#example

ls=[
    {'clc':'penambahan'},
    {'clc':'pengurangian'},
    {'clc':'perkalian'},
    {'clc':'pembagian'}
]
hasil=0
class sys:
    def __init__ (self,ls):
        for i in range(len(ls)):
            print("**initializing-{}**".format(ls[i].get('clc')))
#--------------------------------------------------
    def tambah(self,hasil):
        print("""
        *********Penambahan*********
        """)
        num1=(int(input('nilai a: ')))
        num2=(int(input('nilai b: ')))
        hasil=num1+num2
        print(hasil)
#--------------------------------------------------
    def kurang(self,hasil):
        print("""
        *********Pengurangan*********
        """)
        num1=(int(input('nilai a: ')))
        num2=(int(input('nilai b: ')))
        hasil=num1-num2
        print(hasil)
#--------------------------------------------------
    def kali(self,hasil):
        print("""
        *********Perkalian*********
        """)
        num1=(int(input('nilai a: ')))
        num2=(int(input('nilai b: ')))
        hasil=num1*num2
        print(hasil)
#--------------------------------------------------
    def bagi(self,hasil):
        print("""
        *********pembagian*********
        """)
        num1=(int(input('nilai a: ')))
        num2=(int(input('nilai b: ')))
        hasil=num1/num2
        print(hasil)


f=sys(ls)
# f.tambah(hasil)
# f.kurang(hasil)
# f.kali(hasil)
f.bagi(hasil)