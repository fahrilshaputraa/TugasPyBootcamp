Barang = []
def main():
    print('------------------------------------------------')
    print('        SELAMAT DATANG DI KASIR DEMART        ')
    print('------------------------------------------------')
    while True:
        user = input('Username: ')
        password = input('Password: ')
        if user == 'kasir' and password == 'kasirpass':
            print('Login Berhasil!')
            break
        else:
            print('Maaf Username atau Password salah!')

main()


def DataBarang():
        print('------------------------------------------------')
        nama = input('Masukkan nama item: ')
        harga = int(input('Masukkan harga item: '))
        banyak = int(input('Banyak barang: '))
        tambah_item(nama, harga, banyak)
        print(f'{nama} berhasil ditambahkan!')
        MainKasir()


def tambah_item(nama, harga, banyak):
    Barang.append({'nama': nama, 'harga': harga, 'banyak': banyak})


def pembayaran():
    print('------------------------------------------------')
    total = 0
    for h in Barang:
        total += (int(h['harga'])) * (int(h['banyak']))
    print(f'Total harga: Rp. {total}')

    uang = int(input('Uang Pembeli: '))
    if uang < total:
        print(f'Maaf, uang anda kurang Rp. {total - uang}')
    elif uang > total:
        kembalian = uang - total
        print(f'Kembalian: Rp. {kembalian}')
        banyak = (h['banyak'])
        nama = (h['nama'])
        harga = (h['harga'])
        print('''
                        INDOINDOAN                  
                Alamat: Jln.Alok No. 2829               
                      Telp. 0112972
***********************************************************
                    STRUK PEMBAYARAN                        
***********************************************************
Keterangan                                          Harga''')
        for h in Barang:
            print(f"{h['banyak']} {h['nama']}\t\t\t\t\t\t Rp. {h['harga']}")
        print(f'''
***********************************************************
Total                                               Rp. {total}
Bayar                                               Rp. {uang}
Kembalian                                           Rp. {kembalian}
***********************************************************
                        TERIMA KASIH                        
            Telah membeli barang di tempat kami             
        ''')
    elif uang == total:
         print('Uang pass!')
    exit()


def showBarang():
    print('------------------------------------------------')
    print('Keranjang: ')
    for k in range(len(Barang)):
        print(str(k+1), '. ', Barang[k]['nama'], Barang[k]['harga'],' (',Barang[k]['banyak'],')')
        MainKasir() 
    

def Counterpembayaran():
    print('------------------------------------------------')
    choice = input('Hitung lagi? y/n : ')
    if choice == 'y':
        pembayaran()
    elif choice == 'n':
        MainKasir()


def MainKasir():
    print('========== SELAMAT DATANG DI PROGRAM KASIR ==========')
    print("""MENU APLIKASI
    1. Tambah Barang
    2. Bayar Barang
    3. Keranjang
    4. Log Out""")
    choice = input('Pilih 1-3: ')
    if choice == '1':
        DataBarang()
    if choice == '2':
        pembayaran()
    if choice == '3':
        showBarang()
    if choice == '4':
        exit()
MainKasir()



