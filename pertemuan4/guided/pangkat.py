
bilangan = int(input("Masukkan bilangan: "))
pencacah = int(input("Masukkan pencacah: "))

hasil = 1
for i in range(pencacah):
    hasil *= bilangan
    

print(f"hasil pangkat: {hasil}")
