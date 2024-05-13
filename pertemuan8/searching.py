# dataArray = [1, 2, 55, 34, 67, 99, 87, 300, 201, 344, 233, 123]
# x = int(input("Masukan angka yang ingin dicari: "))
# idx = -1

# for i in range(len(dataArray)):
#     if dataArray[i] == x:
#         idx = i
#         break

# if idx == -1:
#     print('Nilai', x, 'tidak ditemukan dalam list.')
# else:
#     print('Nilai', x, 'ditemukan pada indeks ke-', idx)

dataArray = [1, 2, 55, 34, 67, 99, 87, 300, 201, 344, 233, 123]
dicari = int(input("Masukan angka yang ingin dicari: "))
print("Mencari nilai", dicari, "dengan binary search pada list", dataArray)
ditemukan = False
batas_akhir = len(dataArray) - 1
batas_awal = 0

while not ditemukan and batas_awal <= batas_akhir:
    pos_cari = batas_awal + (batas_akhir - batas_awal) // 2
    print("posisi pencarian: index", pos_cari, 'dengan nilai', dataArray[pos_cari])
    if dataArray[pos_cari] ==  dicari:
        ditemukan = True
    elif dataArray[pos_cari] > dicari:
        batas_akhir = pos_cari - 1
    else:
        batas_awal = pos_cari + 1

if ditemukan:
    print("Nilai", dicari, 'ditemukan pada indeks', pos_cari)
else:
    print("Nilai", dicari, "tidak ditemukan pada list.")