users = [
    {
        'username': 'Kasir',
        'password': '072006'
    }
]
Barang = []
x = "INDOINDOAN"
y = "Alamat: Jln.Alok No.2829"
z = "Telp. 0112972"
a = "STRUK PEMBAYARAN"
m = "TERIMAKASIH!"
n = "Telah membeli barang di tempat kami"

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

    for i in Barang:
        total += (i['harga'] * i['jumlah'])
    print("Total Harga Semua: ", total)

    uang = int(input('Uang Pembeli : '))
    kembali = uang - total
    if kembali >= 0:
        print('Jumlah Kembalian', kembali)
        print('*******************************************************************')
        print()
        print(x.center(50," "))
        print(y.center(50," "))
        print(z.center(50," "))
        print('*******************************************************************')
        print(a.center(50," "))
        print('*******************************************************************')
        print()
        print('Keterangan                                                 Harga   ')
        for s in Barang:
            print(s['jumlah'],s['barang'],'                                                     Rp' ,s['harga'] )
        print('*******************************************************************')
        print('Total                                                     Rp' ,total)
        print('Bayar                                                      Rp' ,uang)
        print('Kembalian                                               Rp' ,kembali)
        print('*******************************************************************')
        print(m.center(50," "))
        print(n.center(50," "))
        exit()
    elif kembali < 0:
        print('Maaf uang anda kurang ', kembali)
        CounterPembayaran(Barang)

def CounterPembayaran(Barang):
    while True:
        pilihan = input('Hitung lagi (y/n) : ')
        if pilihan =='y':
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
            DataBarang(Barang)
            MainKasir()
        elif pilihan == 2:
            if len(Barang) > 0:
                Pembayaran(Barang)
            else:
                print('Anda belum memasukan apa-apa')
        elif pilihan == 3:
            exit()
        else:
            print('Pilihan tidak sesuai')

def Main():
    while True:
        username = input('Username : ')
        password = input('Password : ')
        for q in users:
            if q['username'] == username and q['password'] == password:
                print('Login Berhasil')
                MainKasir()
            else:
                print('Terjadi kesalahan, Silahkan input ulang')

Main()
