bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))


maksimum = max(bilangan1, bilangan2)


for kpk in range(maksimum, bilangan1 * bilangan2 + 1, maksimum):
    if kpk % bilangan1 == 0 and kpk % bilangan2 == 0:
        print("KPK: ", kpk)
        break









