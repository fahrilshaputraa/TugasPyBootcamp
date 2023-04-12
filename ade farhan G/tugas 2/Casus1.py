users = [
    {
    'username':'kasir',
    'password':'kasir'
    }
]
Barang = []

def DataBarang(Barang):
    nama_barang = input('Masukan nama barang : ')
    harga_barang = int(input('Masukan harga barang :'))
    jml_barang = int(input('Masukan jumlah barang : '))

    Barang.append({
        'barang': nama_barang,
        'harga': harga_barang,
        'jumlah': jml_barang
    })

def pembayaran(Barang):
    total = 0
    kembali = 0


    for b in Barang:
        total += (b['harga']) * b['jumlah']
    print('Total Harga Semua: ', total)

    uang = int(input('Uang Pembeli : '))
    kembali = uang - total
    if kembali > 0:
        print('Jumlah kembalian ',        kembali)
        print('=================================')
        print('            INDOBLAZE            ')
        print('=================================')
        print('Keterangan                  Harga')
        for b in Barang:
            print(b['jumlah'],b['barang'], b['harga'])
        print('=================================')
        print('Total                     Rp',-total)
        print('Bayar                     RP',uang)
        print('Kembali                   Rp',kembali)
        
    elif kembali < 0:
        print('Maaf Uang Anda Kurang', kembali)
        CounterPembayaran(Barang)

def CounterPembayaran(Barang):
    while True:
        pilihan = input('Hitung Lagi (y/n) : ')
        if pilihan =='y':
            pembayaran(Barang)
        elif pilihan =='n':
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
                  pembayaran(Barang)
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
        for u in users:
            if u['username'] == username and u['password'] == password:
                print('Login Sukses')
                MainKasir()
            else:
                print('Terjadi kesalahan, Silahkan input ulang')

Main()

