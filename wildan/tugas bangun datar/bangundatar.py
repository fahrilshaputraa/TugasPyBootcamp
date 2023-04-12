    #PERSEGI
def rumusLuas_Persegi():
    print()
    print("========== Menghitung Luas Persegi ==========")
    sisi = int(input("1.Masukan sisi : "))
    luas = int(sisi*sisi)
    print("========== Jawaban ==========")
    print(f"Maka Luas persegi dari sisi {sisi} adalah : {luas}")
    print()
    print ("Terima kasih telah menggunakan program Saya")
       
def rumusKeliling_Persegi():
    print()
    print("========== Menghitung Keliling Persegi ==========")
    sisi = int(input("1.Masukan sisi : "))
    keliling = int(4 * sisi)
    print("========== Jawaban ==========")
    print(f"Maka Keliling persegi dari sisi {sisi}adalah : {keliling}")
    print()
    print ("Terima kasih telah menggunakan program Saya")
    #PERSEGI PANJANG
def rumusLuas_PersegiPanjang():
    print()
    print("========== Menghitung Luas Persegi Panjang ==========")
    panjang = int(input("1.Masukan panjang : "))
    lebar = int(input("2.Masukan lebar : "))
    luas = int(panjang * lebar)
    print("========== Jawaban ==========")
    print(f"Luas persegi panjang dari panjang {panjang}cm lebar {lebar}cm adalah : {luas}")
    print()
    print ("Terima kasih telah menggunakan program Saya")

def rumusKeliling_PersegiPanjang():
    print()
    print("========== Menghitung Keliling Persegi Panjang ==========")
    panjang = int(input("1.Masukan panjang : "))
    lebar = int(input("2.Masukan lebar : "))
    keliling = int((2 * panjang) + (2 * lebar))
    print(f"keliling persegi panjang dari panjang {panjang}cm lebar {lebar}cm adalah : {keliling}")
    print()
    print ("Terima kasih telah menggunakan program Saya")
    #SEGITIGA
def rumusLuas_Segitiga():
    print()
    print("========== Menghitung Luas Segitiga ==========")
    alas=int(input ("1.Masukan Alas: "))
    tinggi=int(input("2.Masukan Tinngi: " ))
    luas= 1/2*alas*tinggi
    print("========== Jawaban ==========")
    print (f"Maka Luas Segitiga dari alas {alas} dan tinggi {tinggi} adalah: ",{luas})
    print()
    print ("Terima kasih telah menggunakan program Saya")

def rumusKeliling_Segitiga():
    print()
    print("========== Menghitung Keliling Segitiga ==========")
    a= int(input("1.Masukkan Sisi 1: "))
    b= int(input("2.Masukkan Sisi 2: "))
    c= int(input("3.Masukkan Sisi 3: "))
    keliling = int(a + b + c)
    print("========== Jawaban ==========")
    print(f"Maka Keliling Segitiga dari sisi 1= {a}, sisi 2= {b}, dan sisi 3= {c} adalah: ",{keliling})
    print()
    print ("Terima kasih telah menggunakan program Saya")
    #LINGKARAN
def rumusLuas_Lingkaran():
    print()
    print("========== Menghitung Luas Lingkaran ==========")
    r = float(input("1.Masukkan nilai jari-jari lingkaran: "))
    phi = 3.14
    luas = phi*r*r
    print("========== Jawaban ==========")
    print(f"Maka Luas lingkaran dari jari-jari {r} adalah : "+ str(luas))
    print()
    print ("Terima kasih telah menggunakan program Saya")
def rumusKeliling_Lingkaran():
    print()
    print("========== Menghitung Keliling Lingkaran ==========")
    r = input("1.Masukkan nilai jari-jari lingkaran: ")
    phi = 3.14
    k = 2 * phi * r
    print("========== Jawaban ==========")
    print(f"Maka Keliling lingkaran dari jari-jari {r} adalah : "+ str(k))
    print("MakaKeliling Lingkaran adalah {}".format(k))
    print()
    print ("Terima kasih telah menggunakan program Saya")