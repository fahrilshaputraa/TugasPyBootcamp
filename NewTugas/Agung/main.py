users = [
    {
        'username': 'Kasir',
        'password': 'Kasir'
    }
]
Barang = []

def DataBarang(Barang):
    nama_barang = input('Masukan nama barang : ')
    harga_barang = int(input('Masukan harga barang : '))
    jml_barang = int(input('Masukan jumlah barang : '))

    Barang.append({
        'barang': nama_barang,
        'harga': harga_barang,
        'jumlah': jml_barang
    })

def Pembayaran(Barang):
    total = 0
    kembali = 0

    for b in Barang:
        total += (b['harga'] * b['jumlah'])
    print('Total Harga Semua: ', total)

    uang = int(input('Uang Pembeli : '))
    kembali = uang - total
    if kembali > 0:
        print('Jumlah Kembalian ', kembali)
        print('*****************************************')
        print('')
        print('              INDOINDOAN                 ')
        print('       Alamat: Jln. Alok No. 2829        ')
        print('            Telp. 082758537              ')
        print('*****************************************')
        print('             STRUK PEMBAYARAN            ')
        print('*****************************************')
        print('Keterangan                        Harga  ')
        for i in Barang:
            print(i['jumlah'],i['barang'],'                         Rp',i['harga'])
        print('*****************************************')
        print('Total                           Rp',total)
        print('Bayar                           Rp',uang)
        print('Kembali                         Rp',kembali)
        print('*****************************************')
        print('              TERIMAKASIH!                ')
        print('    Telah membeli barang ditempat kami    ')
        exit()
    elif kembali < 0:
        print('Maaf uang anda kurang ', kembali)
        print('*************************************')
        CounterPembayaran(Barang)


def CounterPembayaran(Barang):
    while True:
        pilihan = input('Hitung Lagi (y/n) : ')
        if pilihan == 'y':
            Pembayaran(Barang)
        elif pilihan == 'n':
            MainKasir()
        else:
            print('Pilihan tidak sesuai')

def MainKasir():
    while True:
        print('Menu Aplikasi : ')
        print('1. Tambah Barang : ')
        print('2. Bayar Barang : ')
        print('3. Logout : ')

        pilihan = int(input('Pilih 1-3 : '))
        if pilihan == 1:
            print('-------------------------------------------------------------')
            DataBarang(Barang)
            print('-------------------------------------------------------------')
            MainKasir()
        elif pilihan == 2:
            print('-------------------------------------------------------------')
            if len(Barang) > 0:
                Pembayaran(Barang)
            else:
                print('Anda belum memasukan apa-apa')
        elif pilihan == 3:
            print('-------------------------------------------------------------')
            print('Exit Berhasil...')
            exit()
        else:
            print('-------------------------------------------------------------')
            print('Pilihan tidak sesuai')

def Main():
    print('************** SELAMAT DATANG DI KASIR INDOINDOAN **************')
    while True:
        username = input('Username : ')
        password = input('Password : ')
        for u in users:
            if u['username'] == username and u['password'] == password:
                print('Login Berhasil...')
                print('')
                print('*************** SELAMAT DATANG DI PROGRAM KASIR ****************')
                MainKasir()
            else:
                print('Maaf, Username atau Password anda Salah')

Main()