# Nama: Satria Ramadhan
# Kelas: S1-SE07A
# NIM: 2311104026



print("<-   Menu Hitung Biaya Operasi   ->")
print("1. Hitung Biaya Operasi Mata")
print("2. Hitung Biaya Operasi Jantung")
userInput = int(input("Masukan pilihanmu: "))

if userInput == 1:
    print("Masukan Jenis Penyakit MATA")
    print("1. Katarak")
    print("2. Plus/Minus")
    print("3. Silinder")
    userMata = int(input("Masukan jenis panyakit mata: "))
    if userMata == 1:
        print("Biaya Operasi Mata Katarak = Rp. 7.500.000")
    elif userMata == 2:
        print("Biaya Operasi Mata Plus/Minus = Rp. 5.000.000")
    elif userMata == 3:
        print("Biaya Operasi Mata Plus/Minus = Rp. 4.000.000")
    else:
        print("Pilihan tidak valid")
elif userInput == 2:
    print("Masukan Jenis Penyakit Jantung")
    print("1. Jantung Koroner")
    print("2. Katup Jantung")
    print("3. Otot Jantung")
    userJantung = int(input("Masukan jenis penyakit Jantung: "))
    if userJantung == 1:
        print("Biaya Operasi Jantung Koroner = Rp. 500.000.000")
    elif userJantung == 2:
        print("Biaya Operasi Katup Jantung = Rp. 350.000.000")
    elif userJantung == 3:
        print("Biaya Operasi Katup Jantung = Rp. 450.000.000")
    else:
        print("Pilihan tidak valid")
else:
    print("Pilihan tidak valid")