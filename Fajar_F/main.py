users = [
    {
        'username' : 'Kasir',
        'password' : 'Kasir'
    }
]
Barang= []

def DataBarang(Barang):
    nama_barang = input('Masukan nama barang: ')
    harga_barang = int(input('Masukan harga barang: '))
    jml_barang = int(input('Masukan jumlah barang: '))

    Barang.append({
        'barang': nama_barang,
        'harga' : harga_barang,
        'jumlah' : jml_barang

    })

def Pembayaran(Barang):
    total= 0
    kembali= 0

    for b in Barang:
        total += (b['harga']* b['jumlah'])
    print('Total Harga Semua: ', total)

    uang = int(input('Uang Pembeli: '))
    kembali = uang - total
    if kembali > 0:
        print('Jumlah Kembalian ', kembali)
        print('******************************')
        print('         INDOMAKMUR           ')
        print('       Jalan.36 Kawali    ')
        print('**********************************')
        for z in Barang:
                print(z['jumlah'],z['barang'],'         ', z['harga'])
        print('**********************************')
        print('Total                       Rp.',total)
        print('Bayar                       Rp.', uang)
        print('Kembali                     Rp.', kembali)

    elif kembali < 0:
        print('Maaf uang anda tidak mencukupi', kembali)
        counterPembayaran(Barang)

def counterPembayaran(Barang):
    while True:
        pilihan = input('Hitung Lagi (y/n): ')
        if pilihan == 'y':
            Pembayaran(Barang)
        elif pilihan == 'n':
            MainKasir()
        else:
            print('Pilihan tidak sesuai')
def MainKasir():
    while True:
        print('Menu Aplikasi: ')
        print('1. Tambah Barang: ')
        print('2. Bayar Barang: ')
        print('3. Logout: ')

        pilihan = int(input('Pilih 1-3: '))
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
        username = input('username: ')
        password = input('password: ')
        for u in users:
            if u['username'] == username and u['password'] == password:
                print('Login Berhasil')
                MainKasir()
            else:
                print('Terjadi kesalahan')
Main()

