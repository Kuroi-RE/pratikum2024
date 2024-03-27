BilanganBagi = int(input("Masukan bilangan yang akan dibagi: "))
BilanganPembagi = int(input("Masukan bilangan Pembagi: "))

if (BilanganPembagi == 0):
    print("Pembagi tidak boleh 0")
else:
    hasilPembagian = BilanganBagi // BilanganPembagi
    print(f"Hasil bagi: {hasilPembagian}")