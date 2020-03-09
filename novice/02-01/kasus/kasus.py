#-1 f-class fungsi
def greeting():
    print("Hello World")

greeting()
greeting.lang="english"
print(greeting.lang)

#-2 fungsi dalam variable----------------------------------------
sq=lambda x: x*x
sq(5)
foo=sq ; sq(6)
fee=foo ; fee(2)

#-3 fungsi sebagai parameter-------------------------------------
def ind():
    print("bhs.indo")

def en():
    print("english")
def grt(tipe):
    if tipe=="ind":
        ind()
    else:
        en()

grt('ind')

#-4 fungsi yang di operasikan fungsi lain-------------------------
#--a-tanpa
ar=[1,2,3]
arr=[]
for i in range(len(ar)):
    arr.append(ar[i]*2)
arr

#--a-dengan
ar1=[1,2,3]
ar2=[ar1[x]*2 for x in range(len(ar1))]
ar2

#--b-tanpa
lahir=[1975,1997,2002,1995,1985]
umur=[]
for i in range(len(lahir)):
    umur.append(2018-lahir[i])
umur

#-5 array filter-------------------------------------------
name=[
    {'nama':'Piter','umur':16},
    {'nama':'Marek','umur':18},
    {'nama':'Jono','umur':27},
    {'nama':'Jane','umur':14},
    {'nama':'Tono','umur':24}
]
del name
ety_plus=[]
#--atanpa***error***
for i in name:
    if name[i].umur>='18':
        ety_plus.append(name[i])
ety_plus
name
#-6 array reduce------------------------------------------
arr=[5,7,1,8,4]
hasil=0
def s(arr):
    global hasil
    for i in range(len(arr)):
        x=int(arr[i])
        hasil=hasil+x
    return hasil
tambah=s(arr)
tambah