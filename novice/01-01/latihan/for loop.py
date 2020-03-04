n=[]

for i in range(10):
    n.append(i**2)

n

m=list(map(lambda x:x**2,range(10)))
m

o=[x**2 for x in range (10)]
o

#lamda digunakan sebagai function pd python

####################################################################################
[(x,y) for x in[1,2,3] for y in [3,1,4] if x !=y]
#membandingkan nilai x dan y jika nilai tidak sama x dan y akan di cetak

combs=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
combs


vec = [-4,-2,0,2,4]

[x*2 for x in vec]#membuat list baru dengan data yang di gandakan

[x*2 for x in vec if x >= 0]#membuat list dengan nilai yang lebih dari 0 atau bilangan positif saja

[abs(x) for x in vec] #membuat list dengan mengubah semua data menjadi bilangan positif

buah=['pisang','apel','jeruk']
[x.strip() for x in buah]
buah

[(x,x**2) for x in range(6) if x!=0]

vec = [[1,2,3],[4,5,6],[7,8,9]]
[num for x in vec for num in x]

from math import pi
[str(round(pi,i)) for i in range(1,6)]

