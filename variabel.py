##text
# x= 'Hello Purwadhika'
# print(x)
# print(type(x))

##number
# y=20.3
# print('nilai y adalah {}'.format(y))
# print('tipe data y adalah {}'.format(type(y)))

##boolean
# z=22/7==3.14
# print('nilai z adalah {}'.format(z))
# print('tipe data z adalah {}'.format(type(z)))

##koleksi
# list=['jeruk','apel','mangga']
# print('list nya adalah {}'.format(list))
# print('tipe data list adalah {}'.format(type(list)))

# tuple=('jeruk','apel','mangga')
# print('tuple nya adalah {}'.format(tuple))
# print('tipe data tuple adalah {}'.format(type(tuple)))

# dict={'nama':'Baron', 'umur':23}
# print('dictionary nya adalah {}'.format(dict))
# print('tipe data dictionary adalah {}'.format(type(dict)))

##range
# x=range(11)
# print(x)
# print(type(x))

##set
# set={'jeruk','apel','mangga'}
# print('set nya adalah {}'.format(set))
# print('tipe data set adalah {}'.format(type(set)))

##none
# none=None
# print(type(none))

##
# c=123e6
# print(c)
# print(type(c))

# d=123e-6
# print(d)
# print(type(d))

##operasi bilangan
# x=10
# y=3
# z=0
# print('x = {}'.format(x))
# print('y = {}'.format(y))
# print('z = {}'.format(z))
# print('nilai x ditambah y adalah {}'.format(x+y))
# print('nilai x dibagi y adalah {}'.format(x/y))
# print('sisa x dibagi y adalah {}'.format(x%y))
# print('nilai  x floor division y adalah {}'.format(x//y))
# print(f'nilai  x floor division y adalah {x//y} dan nilai x dibagi y adalah {x/y}')

##assignment operator
# x=10
# x+=3
# # x=x+3
# print(x)

##math module
# import math
# x=1.9995
# y=5
# z=4
# print(f'bilangan bulat terdekat yang lebih besar dari {x} adalah {math.ceil(x)}')
# print(f'nilai absolut dari {x} adalah {math.fabs(x)}')
# print(f'bilangan bulat terdekat yang lebih kecil dari {x} adalah {math.floor(x)}')
# print(f'nilai dari {y} dipangkatkan {z} adalah {math.pow(y,z)}')
# print(f'nilai dari akar {math.pow(y,z)} adalah {math.sqrt(math.pow(y,z))}')
# print(f'nilai dari pi adalah {math.pi}')

##casting : merubah tipe data
# x='123'
# print(f'tipe data {x} adalah {type(x)}')
# x=int(x) #casting dari string ke integer
# x=float(x) #casting dari string ke float
# print(f'tipe data {x} adalah {type(x)}')

# x=321234444444444444
# print(f'tipe data {x} adalah {type(x)}')
# x=str(x) #casting dari int ke float
# print(f'tipe data {x} adalah {type(x)}')

##string
# kutipSatu='kutipsSatu("i am Batman")'
# kutipDua="kutipDua(i'm Batman)"
# kutipTiga='''
# "i am Batman" 
# i'm Batman
# '''
# print(kutipSatu)
# print(kutipDua)
# print(kutipTiga)

##escape character
# kutipDua="kutipDua(\"i am Batman\")"
# print(kutipDua)
# kutipTiga=''' kutip tiga bentuknya seperti ini : \'''  '''
# print(kutipTiga)

# ##new line
# kutipDua="i am \n purwadhika student "
# print(kutipDua)

# ##backspace
# kutipDua="i am purwadhika \bstudent "
# print(kutipDua)

# ##tab
# kutipDua="i \tam purwadhika student "
# print(kutipDua)

# x="Halo Dunia"           
# print(f'x adalah {x}')
# ##len
# print(f'panjang karakter {x} adalah {len(x)}')
# ##index
# print(f'karakter Dunia dimulai pada index ke : {x.index("unia")}')
# ##split
# print(x.split(' '))
# ##lower
# print(x.lower())
# ##upper
# print(x.upper())
# ##capitalize
# print(x.capitalize())


# text="i'm_Baron,_nice_to_meet_you"
# print(text[1])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[-1])
# print(text[-3:-1]) #-3,-2

# x='Apel'
# y='Jeruk'
# print(x+y)
# print(x+' '+y+'5')

# jumlahApel=3
# jumlahJeruk=5
# pembelian="Saya mau beli {} Apel, {} Mangga, dan {} Jeruk."
# print(pembelian.format(jumlahApel,7,jumlahJeruk))
# print("Saya mau beli {} Apel, {} Mangga, dan {} Jeruk.".format(jumlahApel,7,jumlahJeruk))
# print(f"Saya mau beli {jumlahApel} Apel, {7} Mangga, dan {jumlahJeruk} Jeruk.")

# username=input('Masukkan username Anda : ')
# print('Username Anda adalah : '+ username)

##soal 1
# x=4
# y=3
# z=2
# w=((x+y*z)/(x*y))**z
# print(w)

# ##soal 2
# angka=float(input('masukkan angka berapapun :'))
# print(f'kuadrat dari {angka}={angka**2}')

##soal 3
# x=485 #hari
# # Tahun
# Tahun=x//360
# # Bulan
# Bulan=(x-360*Tahun)//30
# # Minggu
# Minggu=(x-360*Tahun-30*Bulan)//7
# # Hari
# Hari=x-360*Tahun-30*Bulan
# print(f'{x} Hari dalam Tahun, Bulan, Minggu, dan Hari adalah {Tahun} Tahun,{Bulan} Bulan, {Minggu} Minggu dan {Hari} Hari')

##soal 4
#rasio andi/budi=4/10 -> rasio andi = 4, rasio budi = 10
total_umur=49
rasio_andi=4
rasio_budi=10
rasio_total=14
usia_andi=(rasio_andi/rasio_total)*total_umur
usia_budi=(rasio_budi/rasio_total)*total_umur
# print(f'usia andi dan budi berturut-turut adalah {usia_andi} tahun dan {usia_budi} tahun')
print(f'usia andi dan budi 2 tahun lagi berturut-turut adalah {usia_andi+2} tahun dan {usia_budi+2} tahun')

import math
##soal 5
jarak=120
kecepatanA=60
kecepatanB=40
jam_sekarang=9
#kecepatan=jarak/waktu
#waktu=jarak/kecepatan
jam=(jarak//(kecepatanA+kecepatanB))
menit=int(((jarak/(kecepatanA+kecepatanB))-jam)//(1/60))
print(f'dua mobil bertabrakan pada jam {jam_sekarang+jam}:{menit} WIB')


