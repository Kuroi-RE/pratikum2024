inputUser = int(input("Masukan suhu: "))


if inputUser <= 0:
    print("Suhu beku 🥶🥶🥶")
elif inputUser > 0 and inputUser < 100:
    print("Suhu cair")
elif inputUser > 100:
    print("Suhu uap")