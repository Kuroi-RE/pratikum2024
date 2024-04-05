
bilangan = int(input("Masukan bilangan: "))

total = 0

langkah_penjumlahan = ""


for i in range(bilangan, 0, -1):
    total += i
    langkah_penjumlahan += str(i) + " "
    if i != 1:
        langkah_penjumlahan += "+ "

print(f"Total Nilai: {langkah_penjumlahan} = {total}")
