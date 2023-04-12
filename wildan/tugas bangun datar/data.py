from bangundatar import rumusLuas_Persegi, rumusKeliling_Persegi, rumusLuas_PersegiPanjang, rumusKeliling_PersegiPanjang, rumusLuas_Segitiga, rumusKeliling_Segitiga, rumusLuas_Lingkaran, rumusKeliling_Lingkaran
def persegi():
    print("1. Luas persegi")
    print("2. Keliling persegi")
    pilihan = input("Masukkan Rumus yang akan anda gunakan: ")
    while True:
        if pilihan == "1":
            rumusLuas_Persegi()
            break
        elif pilihan == "2":
            rumusKeliling_Persegi()
            break
        else:
            pilihan= input("Maaf, pilihan anda tidak tersedia. Pilih Kembali: ")

def persegi_panjang():
    print("1. Luas persegi Panjang")
    print("2. Keliling persegi Panjang")
    pilihan = input("Masukkan Rumus yang akan anda gunakan: ")
    while True:
        if pilihan == "1":
            rumusLuas_PersegiPanjang()
            break
        elif pilihan == "2":
            rumusKeliling_PersegiPanjang()
            break
        else:
            pilihan= input("Maaf, pilihan anda tidak tersedia. Pilih Kembali: ")

def Segitiga():
    print("1. Luas Segitiga")
    print("2. Keliling Segitiga")
    pilihan = input("Masukkan Rumus yang akan anda gunakan: ")
    while True:
        if pilihan == "1":
            rumusLuas_Segitiga()
            break
        elif pilihan == "2":
            rumusKeliling_Segitiga()
            break
        else:
            pilihan= input("Maaf, pilihan anda tidak tersedia. Pilih Kembali: ")

def Lingkaran():
    print("1. Luas Lingkaran")
    print("2. Keliling Lingkaran")
    pilihan = input("Masukkan Rumus yang akan anda gunakan: ")
    while True:
        if pilihan == "1":
            rumusLuas_Lingkaran()
            break
        elif pilihan == "2":
            rumusKeliling_Lingkaran()
            break
        else:
            pilihan= input("Maaf, pilihan anda tidak tersedia. Pilih Kembali: ")        
