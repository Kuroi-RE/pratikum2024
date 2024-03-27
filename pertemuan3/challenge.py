user = input("Apakah kamu perempuan/laki-laki?: ").lower()

if user == "perempuan":
    perempuanInput = input("Apakah kamu sudah menikah? [iya/tidak]: ")
    if perempuanInput == "iya":
        print("kamu adalah seorang ibu")
    elif perempuanInput == "tidak":
        print("Kamu masih seorang mbak-mbak")
    else:
        print("Jawaban tidak valid")
elif user == "laki-laki":
    lakiInput = input("Apakah kamu sudah menikah? [iya/tidak]: ")
    if lakiInput == "iya":
        print("kamu adalah seorang bapak")
    elif lakiInput == "tidak":
        print("kamu masih seorang mas-mas")
    else:
        print("Jawaban tidak valid")
    