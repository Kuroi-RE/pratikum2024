def MencariLuas(jari_jari):
    Luas = 3.14 * jari_jari * jari_jari
    return Luas

def MencariKeliling(jari_jari):
    Keliling = 2 * 3.14 * jari_jari
    return Keliling


jari_jari = int(input("Masukan jari jari : "))

print(f"Keliling Lingkaran : {MencariKeliling(jari_jari)}\nLuas Lingkaran : {MencariLuas(jari_jari)}")

