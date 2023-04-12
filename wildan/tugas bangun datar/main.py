from data import persegi, persegi_panjang, Segitiga, Lingkaran

print('SELAMAT DATANG DI PROGRAM BANGUN DATAR')
print('======================================')

def data():
    print("Pilih menu berikut :")
    print('__________________')
    print("1. Rumus Persegi")
    print("2. Rumus Persegi Panjang")
    print("3. Rumus Segitiga")
    print("4. Rumus Lingkaran")
    print('=========================')

    pilihan = input("Masukkan Rumus yang akan anda gunakan: ")
    while True:
        if pilihan == "1":
            persegi()
            break
        elif pilihan == "2":
            persegi_panjang()
            break
        elif pilihan == "3":
            Segitiga()
            break
        elif pilihan == "4":
            Lingkaran()
            break
        else:
            pilihan=input("Maaf, pilihan tidak tersedia")
data()