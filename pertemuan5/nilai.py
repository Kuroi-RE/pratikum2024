countMatkul = int(input("Masukan Jumlah mata kuliah: "))
nilai = []


for i in range(countMatkul):
    nilaiUser = float(input(f"Masukan nilai mata kuliah ke-{i + 1}: "))
    nilai.append(nilaiUser)

valid = True
for nilaiUser in nilai:
    if nilaiUser < 0 or nilaiUser > 100:
        valid = False
        break


if not valid:
    print("Nilai tidak valid!")
else:
    rata_rata = sum(nilai) / len(nilai)
    
    if rata_rata >= 90:
        predikat = "A"
    elif rata_rata >= 70:
        predikat = "B"
    elif rata_rata >= 50:
        predikat = "C"
    elif rata_rata >= 30:
        predikat = "D"
    else:
        predikat = "E"
        
    print("=====================================")
    print(f"Hasil predikat {predikat} dengan nilai:")
    
    for i in range(len(nilai)):
        print(f"Nilai mata kuliah ke-{i + 1}: {nilai[i]}")
