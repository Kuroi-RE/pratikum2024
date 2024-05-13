# Pada suatu organisasi memiliki 10 anggota dengan nama masing-masing : Pain,
# Konan, Tobi, Zetsu, Sasori, Hidan, Deidara, Kisame, Kakuzu, dan Itachi . Supaya
# mudah dalam melakukan pencarian, Ketua organisasi akan mengurutkan nama-
# nama tersebut sesuai dengan alfabet. Buatlah program untuk membantu Pain
# dengan menggunakan algoritma Selection Sort!

def SortAkatsuki(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

anggota_akatsuki = ["Pain", "Konan", "Tobi", "Zetsu", "Sasori", "Hidan", "Deidara", "Kisame", "Kakuzu", "Itachi"]

print(f"Anggota akatsuki: {SortAkatsuki(anggota_akatsuki)}")