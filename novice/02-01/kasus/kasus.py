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

#print(name[int('1')].get("umur"))
ety_plus=[]
#--atanpa***error***
for i in range(len(name)):
    a = name[i].get("umur")
    if a>=18:
        ety_plus.append(name[i].get('nama'))
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
    return hasil+10
tambah=s(arr)
tambah

arr=['javascript','python','php','java','c']
ar=[]
def ls(arr):
    for i in range(len(arr)):
        a=arr[i]
        ar.append(len(a))
ls(arr)
ar
