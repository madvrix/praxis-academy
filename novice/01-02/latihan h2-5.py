#5.2 del################################
a=[-1,1,66.25,333,333,1234.5]
del a[0]#menghapus data ke 0 dari a
a
del a[2:4]#menghapus data antara data ke 2 dan ke 4
a
del a[:]#menghapus semua data

del a #menghapus variable

tupl=12345, 54321, 'hwgko'
tupl[0];t[1];t[2]
tupl

v=[(3,2,1),(1,2,3)]
v=([1,2,3],[3,2,1])
v

#5.3 set()#############################
basket={'apple','orange','apple','pear','orange','banana'}
print (basket)#jika menggunakan {} maka data yang berupa duplikat atau sama di anggap satu dan di hilangkan
'apple' in basket#cek keanggotaan dalam basket
#jika ada maka bernilai true jika tidak maka false

a=set('absjfj2iej')
b=set('1824ujdahwjdajwd')
a;b
b-a#b yang tidak ada di a
b|a#semua dari a dan b
b&a#yang sama dari a dan b
b^a#semua dari a dan b yang tidak sama

#set comprehension
a={x for x in 'abracadabra' if x not in 'abc'}
a

#5.4 dictionary#########################
tel={'jack':['awdsawd','awdasdwa',1231],'kili':312}
tel['lulo']=321#menambahkan list
tel
tel['jack']#menampilkan data jack
del tel['jack']
tel['jack']
list(tel)#hanya ,menampilkan nama tidak beserta data

#5.5 teknik perulangan************************************
#**list dengan data 1:A 2:B 3:C
sort={'a':'12345','b':'54321'}
for x, y in sort.items():
    print(x,y)
print(sort)

#**list dengan data 1 2 3
for i, j in enumerate(['aaa','bbb','ccc']):
    print (j,i)
print ("same tm")

#**list dengan data A:1 & B:1 ; A:2 & B:2....
A=[1,3,5]
B=['2','4','6']
C=['a','b','c']
for a,b,c in zip(A,B,C):
    print("data {0} & {1} di {2}".format(a,b,c))
print("multi")

#**perhitungan mundur"reversed()"
for i in reversed(range(0,11,2)):#batas 0-11 || %2
    print(i,end=",")
"cek"

#**