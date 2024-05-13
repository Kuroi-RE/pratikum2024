def ganjil(n:int):
    return  n % 2 == 1

def genap(n:int):
    return n % 2 == 0

user_angka = input("Masukan bilangan : ")


# Validasi inputan angka menggunakan fungsi yang telah kita buat.
if user_angka.isdigit():
    angka = int(user_angka)
    if ganjil(angka): 
        print("Bilangan yang anda masukan adalah Ganjil")
    elif genap(angka): 
        print("Bilangan yang anda masukan adalah Genap")
else: # jika inputan selain ganjil dan genap maka akan menghasilkan pesan Input tidak valid.
    print("Input yang anda masukan tidak valid!")

    