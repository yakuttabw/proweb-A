print('Program Membuat Matriks')
pil=-1
while pil!=2:
    print(''' Menu: 
    1. Membuat Matriks 
    2. Keluar''')

    pil=int(input('Masukkan pilihan anda : '))

    if pil==1:
        a=int(input('masukkan a: '))
        b=int(input('masukkan b: '))
        c=int(input('masukkan c: '))
        d=int(input('masukkan d: '))
        matriks=[[a,b],[c,d]]
        for x in matriks : print (x)
    elif pil==2:
        print('Terima Kasih sudah menggunakan ini.')
    else: print('Masukkan pilihan yang ada di menu.')






