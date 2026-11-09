kata_pertama = "dio "
kata_kedua = "jebew"

for angka in range(1,31):
    aturan1 = (angka % 4 == 0)  # aturan pertama = kelipatan 4
    aturan2 = (angka % 6 == 0)  # aturan kedua = kelipatan 6

    if aturan1 and aturan2:
        print(kata_pertama + kata_kedua)
    elif aturan1:
        print(kata_pertama)
    elif aturan2:
        print(kata_kedua)
    else:
        print(angka)

print()