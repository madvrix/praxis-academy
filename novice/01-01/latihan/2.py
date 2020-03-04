'spam eggs' #mencetak string menggunakan tanda kutip satu

'doesn\'t'  # (\)digunakan agar tanda kutip yang di gunakan tidak menutup syntax string atau apalah
"doesn't"   # atau gunakan "" jika ingin menggunakan '' dalam string
'"yes",they said' #begitujuga sebaliknya ketika menggunakan "" dalam string 

print('i don\'t\n know') #\n digunakan untuk berganti baris dengan ketentuan string di cetak dengan perintah (print)
tx='uh yeahhh \na-fel gd nw'
print(tx)

print('c:\some\dir\name')#dalam permasalahan berikut '\n' dari '\name' diangganp sebagai new line
print(r'c:\some\dir\name')#penulisan r sebelum string mengubah \ menjadi spesial karakter sehingga '\n' dari '\name' tidak di anggap sebagai syntax untuk membuat baris baru

print("""\
usage: thingy [options]
        -h\                         Display this usage mesage
        -H hostname                 Hostname to connect to


""")
#("""...""") atau ('''...''') digunakan untuk mencetak string sesuai dengan span yang di gunakan

'uh'+'y'+50*'e'+'aaah'#penggunaan operator + bisa digunakan untuk menggabungkan string dan *50 digunakan untuk mencetak string sebanyak 50x

'py''thon' 'python' ' python' #dua string yang tidak memiliki spasi di bagian belakang atau depan akan menyatu menjadi satu
                              #sangat berguna ketika ingin memotong string yang panjang
text=('lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum '
     '2 lorem ipsum lorem ipsum lorem ipsum lorem ipsum ')
text

text2='uhhh'
text2+'  yeahh' #error akan terjadi jikka penggabungan variable dengan string dilakukan secara langsung 

('un'*5+'cccch') 'iiwwwee'#hanya menampilkan eror kecuali jika setelah tutup kurung di beri tanda +
('un'*5+'cccch')+ 'iiwwwee'

word='mamank'
word[4]#mencetak karakter ke-empat dari variable word 'hitungan dimulai dari 0'
word[-1]#mencetak karakter terakhir dari var word
word[-2]#mencetak karakter terakhir kedua dari var word
word[2:5]#mencetak karakter ke-dua hingga ke-lima dari var word
word[2:]+word[:2]+word[2:]#menggabungkan karakter perbagian kata
word[-2:]
word[5]='a'#error ketika melakukan assignment dengan cara tersebut

texx='ajkdvukadvlbdnsbkowlidbkasdv,aiwdwfavdmahdw'
tex='12345'
len(tex)#hasil43
len(texx)#hasil5
#len digunakan untuk menampilkan jumlah karakter pada string
