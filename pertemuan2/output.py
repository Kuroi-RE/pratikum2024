print("Belajar program python")

belajar = "belajar pemrograman 1"

print(belajar) # Print variable

print("Hallo {}".format(belajar)) #Print variable with Format


nama = "Satria Ramadhan"

print("Hallo selamat pagi {}".format(nama))

seng = "Mendoan"
gilang = "Tahu"
zidan = "Soto"

print("Kesukaan seng = "+str(seng), "\n Kesukaan gilang = "+str(gilang), "\n Kesukaan zidan = "+str(zidan)) # print beberapa variabel menggunakan fungsi str

print("Kesukaan seng = {}, kesukaan gilang = {}, kesukaan zidan {}".format(seng, gilang, zidan)) # print beberapa variabel menggunakan fungsi format

print(f"Kesukaan seng = {seng} \n Kesukaan gilang = {gilang}\nKesukaan zidan = {zidan}") # print beberapa variabel menggunakan f""

# rumus

panjang = 10
lebar = 5
luas = panjang * lebar

print("luas = ", luas) # print without +
print("luas = "+str(luas)) # format variabel ke string