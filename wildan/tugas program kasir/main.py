users = [
    {
        'username' : 'kasir',
        'password' : 'kasirpass'
    }
]
Barang = []

def DataBarang(Barang):
    nama_barang = input('Masukan nama barang :')
    harga_barang = int(input('Masukan haraga barang :'))
    jml_barang = int(input('Masukan jumlah barang :'))

    Barang.append({
        'barang' : nama_barang,
        'harga' : harga_barang,
        'jumlah' : jml_barang
    })
def Pembayaran(Barang):
    total = 0
    kembali = 0

    for b in Barang:
        total += (b['harga'] * b['jumlah'])
    print('Total harga :', total)

    uang = int(input('Uang pembeli :'))
    kembali = uang - total
    if kembali > 0:
        print('Jumlah kembalian :', kembali)
        print('*****************************')
        print('       INDODANZMART          ')
        print('*****************************')
        print('Keterangan :                     Harga :')
        for z in Barang:
                print(b['jumlah'],b['barang'],          b['harga'])
        print('******************************')
        print('Total                 Rp',total)
        print('Bayar                  Rp',uang)
        print('Kembali             Rp',kembali)
        exit()

    elif kembali < 0:
        print('Mohon maaf uang anda tidak cukup', kembali)
        CounterPembayaran(Barang)
def CounterPembayaran(Barang):
    while True:
        pilihan = input('Hitung lagi (yes/no) :')       
        if pilihan == 'yes':
            Pembayaran(Barang)
        elif pilihan == 'no':
            MainKasir()
        else:
            print('Pilihan tidak sesuai !')

def MainKasir():
    while True:
        print('     ===Menu Aplikasi===     ')
        print('1. Tambah Barang :')
        print('2. Bayar Barang :')
        print('3. Logout :')
        
        pilihan = int(input('pilih 1/2/3 :'))
        if pilihan == 1:
            DataBarang(Barang)
      
        elif pilihan == 2:
            if len(Barang) > 0:
                Pembayaran(Barang)
            else:
                print('Anda belum memasukan apapun !')
        elif pilihan == 3:
            exit()
        else:
            print('Pilihan tidak sesuai !!!')
            
def Main():
    while True:
        username = input('Username :') 
        password = input('Password :')
        for y in users:
            if y['username'] == username and y['password'] == password:
                print('Login Berhasil')
                MainKasir()
            else:
                print('Mohon maap terjadi kesalahan !!!')

Main()
