    # 1 = pejumplahan
    # 2 = perkalian
    # 3 = pengurangan
    # 4 = pangkat

def pejumlahan(bil1, bil2):
    return bil1 + bil2
def perkalian(bil1, bil2):
    return bil1 * bil2
def pengurangan(bil1, bil2):
    return bil1 - bil2
def pangkat(bil1, bil2):
    return bil1 ** bil2

print("KALKULATOR")
print("1. Pejumlahan\n2. Perkalian\n3. Pengurangan\n4. Pangkat")
pilihan_pengguna = int(input("Masukan Pilihan : "))

if pilihan_pengguna == 1:
    bilangan1 = int(input("Masukan Bilangan pertama: "))
    bilangan2 = int(input("Masukan Bilangan kedua: "))
    print(f"Hasil pejumlahan : {pejumlahan(bilangan1, bilangan2)}")
elif pilihan_pengguna == 2:
    bilangan1 = int(input("Masukan Bilangan pertama: "))
    bilangan2 = int(input("Masukan Bilangan kedua: "))
    print(f"Hasil perkalian : {perkalian(bilangan1, bilangan2)}")
elif pilihan_pengguna == 3:
    bilangan1 = int(input("Masukan Bilangan pertama: "))
    bilangan2 = int(input("Masukan Bilangan kedua: "))
    print(f"Hasil pengurangan : {pengurangan(bilangan1, bilangan2)}")
elif pilihan_pengguna == 4:
    bilangan1 = int(input("Masukan Bilangan pertama: "))
    bilangan2 = int(input("Masukan Bilangan kedua: "))
    print(f"Hasil pangkat : {pangkat(bilangan1, bilangan2)}")
else:
    print("Pilihan tidak ada dalam Menu!")