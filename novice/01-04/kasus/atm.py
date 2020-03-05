saldo=0
def tambah(saldo):
        print ("""
        Masukan nominal yang akan ditabung
         = """,end="Rp.")
        nilai=int(input())
        saldo=saldo+nilai
        return saldo
def tarik(saldo):
        print ("""
        Masukan nominal yang akan diambil
         = """,end="Rp.")
        nilai=int(input())
        saldo=saldo-nilai
        return saldo
def cek(saldo):
        print("""
        Saldo yang anda miliki adalah
         = Rp.""",saldo)
def pilih(pilihan,saldo):
        saldo=saldo
        if pilihan==1:
            cek(saldo)
        elif pilihan==2:
            saldo=tambah(saldo)
            print("""
            """)
        elif pilihan==3:
            saldo=tarik(saldo)
        else:
            print("input yang anda masukan salah")
            pilih(input(),saldo)

##saldo=tarik(saldo) >>>update setelah tarik saldo
##saldo=tambah(saldo) >>>update setelah tambah
##cek(saldo) >>>cek nilai saldo
print("""

-------------ATM PYTHON-------------

->(1)Cek saldo     ->(3)Tarik Tunai
->(2)Setor Tunai

------------------------------------

Masukan layanan yang anda inginkan
---------------(1/2/3)--------------
""")

pilihan=int(input("---->"))
pilih(pilihan,saldo)