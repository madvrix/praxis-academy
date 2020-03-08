###########control flow tools#############

#4.1 if statment
x=int(input("masukan angka : "))
if x < 0:
    x=0
    print('bilangan negatif diubah ke 0')
elif x==0
    print('zero')
elif x==1:
    print('single')
elif:
    print('more')

#4.2 for
kata=['kucing','jendela','lantai']
for w in kata:
    print(w, len(w))
print('---')

#4.3 range()
lis=['1','2','3','4','5']
for i in range(5):
    print (i,lis[i])
"cek"

range(5,10)#5-10
range(0,10,3)#kelipatan 3 dengan batas atas 10 (0,3,6,9)
range(-10,-100,-30)#kelipatan -30 dengan batas 100(-10,-40,-70)

a=['saya','berusaha','memahami','bahasa','ini']
for i in range(len(a)):#len(a) = banyak data dalam a (5)
    print (i,a[i])
"cek"

print(range(10))
sum(range(5))#menjumlahkan range yang di tentukan
list(range(5))#mencetak range yang di tentukan

#4.4 break,continue dan else klausa

for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n,' sama dengan ',x,' * ', n)
            break
        else:
            print(n,'bilangan prima')
            break
#break melewati statement for terdalam lalu menuju ke nilai for selanjutnya
'cek'

#4.5 pass
while True:
    pass

class empty:
    pass

def fungsi:
    pass

#pernyataan pass tidak melakukan perintah apapun, tapi pass dapat di gunakan ketika perintah dibutuhkan tapi tidak ada perintah yang diperlukan

#4.6 Fungsi

