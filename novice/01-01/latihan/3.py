sq=[1,4,9,16,25]
sq
sq[:]
sq[2:]
sq+[36,49,81,100]
sq

ar=[1,8,27,65,125]
ar[3]=64#mengganti value ar ke 3 dengan 64
ar
ar.append(216)
ar.append(7**2)
ar.pop()
ar.append(7**3)

lt=['a','b','c','d','e','f','g']
lt
lt[:3]=['A','B','C','D'] #mengganti beberapa value sekaligus
lt[2:5]=[]#jika value ke2 sampai ke 5 di ganti [] 'kosong' maka value akan hilang
lt
lt[:]=[]
lt#maka lt akan kosong 
lt=['a','b','c','d']
len(lt)#menghitung banyak data dalam lt

a=['a','b','c']
n=[1,2,3]
x=[a,n]#mendeklarasikan array x dengan array a sebagai data ke 1 dan array n sebagai data kedua
a;n
x#data tetap di tampilkan berbentuk array sendiri sendiri

#perulangan untuk menentukan bil.fibonacci
a,b=0,1
while a<10:
    print (a)
    a,b=b,a+b
a

i=256*256
print('nilai dari i :',i)

a,b=0,1
while a < 1000:
        print(a,end=',')

        a,b=b,a+b
a,b