Barang = []
kasir = [
    {
    'username' : 'fitri',
    'password' : '271006',
    }
]


def DataBarang():
        print("-------------------------------------------------------------------------------")
        name = input("Masukkan nama barang : ")
        price = input("Masukkan harga barang : ")
        lots = input("Masukkan banyak barang : ")
        print("-------------------------------------------------------------------------------")
        Barang.append({'name' : name, 'price' : price, 'lots' : lots})
        print("Barang berhasil ditambahkan !")
        print(" ")


def Pembayaran():
    print("-------------------------------------------------------------------------------")
    total_harga = 0
    for h in Barang:
        total_harga += ((int(h['price'])) * (int(h['lots'])))
    print(f"Total harga semua : Rp. {total_harga}")

    uangP = int(input("Uang pembeli Rp. "))
    if uangP < total_harga:
        kurang = total_harga - uangP
        print(f"Maaf uang anda kurang Rp. {kurang}")
        print ("*******************************************************************************")
        CounterPembayaran()

    elif uangP > total_harga:
        kembalian = uangP - total_harga
        print(f"Jumah kembalian Rp. {kembalian}")
        print(" ")
        print ("*******************************************************************************")
        print('''
                                  INDOINDOAN
                           Alamat: Jln.Alok No.2829
                                Telp. 0112972
*******************************************************************************
                                STRUK PEMBAYARA
*******************************************************************************
Keterangan                                                      Harga
        ''')
        for h in Barang:
            print(f"{h['lots']} {h['name']} \t\t\t\t\t\t\t\t {h['price']}")
        print(f'''
*******************************************************************************
Total                                                           {total_harga}   
Bayar                                                           {uangP}
Kembalian                                                       {kembalian}
*******************************************************************************
                                  TERIMAKASIH
                       Telah membeli barang di tempat kami
        ''')
    elif uangP == total_harga:
        print('Uang pass')
    exit()

def CounterPembayaran():
    counter = input("Hitung lagi ? (y/n)")
    if counter == 'y':
        Pembayaran()
    elif counter == 'n':
        MainKasir()

def ShowBarang():
    print("-------------------------------------------------------------------------------")
    print('Daftar barang :')
    for u in range(len(Barang)):
        print(str(u+1), '. ', Barang[u]['name'], Barang[u]['price'], ' (',Barang[u]['lots'],')')

# menu opsi
def MainKasir():
    while True:
        print(" ")
        print("+++++++++++++++++++++++ SELAMAT DATANG DI PROGRAM KASIR +++++++++++++++++++++++")
        choice = input('''MENU APLIKASI :
1. Tambah barang
2. Bayar barang
3. Lihat barang
4. Logout
Pilih 1-3 : ''')
        if choice == '1':
            DataBarang()
        elif choice == '2':
            Pembayaran()
        elif choice == '3':
            ShowBarang()
        elif choice == '4':
            exit()
    

# Menu Login
def main():
    while True:
        print("++++++++++++++++++++ SELAMAT DATANG DI KASIR WARUNG MAKAN ++++++++++++++++++++")
        username = input('Masukkan username kasir : ')
        password = input('Masukkan password kasir : ')
        for i in kasir:
            if i['username'] == username and i['password'] == password:
                print("Login Berhasil.....")
                if True:
                    MainKasir()
                break
            else:
                print("Maaf, Username atau Password anda salah.....")
main()