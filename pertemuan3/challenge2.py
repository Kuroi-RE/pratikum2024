nama = input("Nama kamu: ")
jenisKelamin = input("Jenis Kelamin: ")
agama = int(input("Agamamu: "))


# Tidak efesien
# if agama == 1:
#     print(f"Namamu {nama}, jenis kelaminmu adalah {jenisKelamin} dan agamamu Islam")
# elif agama == 2:
#     print(f"Namamu {nama}, jenis kelaminmu adalah {jenisKelamin} dan agamamu Kristen")
# elif agama == 3:
#     print(f"Namamu {nama}, jenis kelaminmu adalah {jenisKelamin} dan agamamu Protestan")
# elif agama == 4:
#     print(f"Namamu {nama}, jenis kelaminmu adalah {jenisKelamin} dan agamamu Hindu")
# elif agama == 5:
#     print(f"Namamu {nama}, jenis kelaminmu adalah {jenisKelamin} dan agamamu Buddha")
# else:
#     print(f"Namamu {nama}, jenis kelaminmu adalah {jenisKelamin} dan Atheiss??!!")

if agama == 1:
    agama = "Islam"
elif agama == 2:
    agama = "Kristen"
elif agama == 3:
    agama = "Protestan"
elif agama == 4:
    agama = "Hindu"
elif agama == 5:
    agama = "Buddha"
else:
    agama = "Atheis"


print(f"Nama kamu {nama} kamu seorang {jenisKelamin} agamamu {agama}")