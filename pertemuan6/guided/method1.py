def nama_fungsi():
    print("Ini method fungsi")


nama_fungsi()

def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    return f"luas: {luas}\nkeliling: {keliling}"

print("luas persegi: %d" % keliling_luas_persegi(10))

def luas_persegipanjang(panjang, lebar):
    luas = panjang * lebar
    print("Luas persegi panjang: %d" % luas)

luas_persegipanjang(10, 7)

def luas_segitiga(alas, tinggi):
    luas = alas * tinggi / 2 
    return luas

print("Luas segitiga: %d" % luas_segitiga(6, 10))