saldo=0
def tambah(pilihan,saldo):
        print ("""
Masukan nominal yang akan ditabung
= """,end="Rp.")
        nilai=int(input())
        saldo=saldo+nilai
        print("""

------------------------------------------
        Lakukan transaksi lagi?
        
        """)
        prom=input("Y/N")
        pilihan=0
        if prom=="Y" or prom=="y":
            menu()
            pilih(int(input("---->")),saldo)
        return saldo


def tarik(pilihan,saldo):
        print ("""

------------------------------------------

Masukan nominal yang akan diambil
= """,end="Rp.")
        nilai=int(input())
        saldo=saldo-nilai
        print("""

------------------------------------------
        Lakukan transaksi lagi?
        
        """)
        prom=input("Y/N")
        pilihan=0
        if prom=="Y" or prom=="y":
            menu()
            pilih(int(input("---->")),saldo)
        return saldo


def cek(pilihan,saldo):

        print("""

------------------------------------------

Saldo yang anda miliki adalah
= Rp.""",saldo)
        print("""

------------------------------------------
        Lakukan transaksi lagi?
        
        """)
        prom=input("Y/N")
        pilihan=0
        if prom=="Y" or prom=="y":
            menu()
            pilih(int(input("---->")),saldo)

def pilih(pilihan,saldo):
        saldo=saldo
        if pilihan==1:
            cek(pilihan,saldo)
        elif pilihan==2:
            saldo=tambah(pilihan,saldo)
            print("""
            """)
        elif pilihan==3:
            saldo=tarik(pilihan,saldo)
        else:
            print("""
------------------------------------------
Input yang anda masukan salah..!
silahkan masukan input anda
""")
            pilih(int(input("---->")),saldo)

##saldo=tarik(saldo) >>>update setelah tarik saldo
##saldo=tambah(saldo) >>>update setelah tambah
##cek(saldo) >>>cek nilai saldo
def menu():
    print("""

-------------   ATM PYTHON   -------------

    ->(1)Cek saldo     ->(3)Tarik Tunai
    ->(2)Setor Tunai

------------------------------------------

    Masukan layanan yang anda inginkan
------------------(1/2/3)-----------------
""")
menu()
pilihan=int(input("---->"))
pilih(pilihan,saldo)
