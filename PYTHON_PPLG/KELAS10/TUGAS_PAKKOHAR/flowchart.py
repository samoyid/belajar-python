import math
def input_positif(teks):
    while True:
        try:
            val = float(input(teks))
            if val > 0:
                return val
            print("!! NILAI HARUS LEBIH BESAR DARI 0 !!")
        except ValueError:
            print("!! MASUKAN ANGKA YANG VALID !!")

print("= = PROGRAM ALGORITMA LUAS BANGUN DATAR = =")
print("NAMA: DIO NAZRIL FALEVI")
print("KELAS: X RPL 1")
print("ABSEN: 17")
print("MAPEL: PPLG (PAK KOHAR)")

while True:
    print("\nMENU PILIHAN BANGUN DATAR:")
    print("1. persegi")
    print("2. persegi panjang")
    print("3. lingkaran")
    print("4. jajar genjang")
    print("5. trapesium")
    print("6. belah ketupat")
    print("7. layang-layang")
    print("8. setengah lingkaran")
    print("9. segi enam beraturan")
    print("10. segitiga")
    print("0. keluar")
    try:
        p = int(input("MASUKAN PILIHAN (0-10): "))
    except ValueError:
        print("!! PILIHAN HARUS ANGKA !!")
        continue
    nama = None
    luas = None
    if p == 0:
        break
    elif p == 1:
        s = input_positif("MASUKAN SISI: ")
        luas = s * s
        nama = "PERSEGI"
    elif p == 2:
        pjg = input_positif("MASUKKAN PANJANG: ")
        lbr = input_positif("MASUKKAN LEBAR: ")
        luas = pjg * lbr
        nama = "PERSEGI PANJANG"
    elif p == 3:
        r = input_positif("MASUKKAN JARI - JARI: ")
        luas = math.pi * r * r
        nama = "LINGKARAN"
    elif p == 4:
        a = input_positif("MASUKKAN ALAS: ")
        t = input_positif("MASUKKAN TINGGI: ")
        luas = a * t
        nama = "JAJAR GENJANG"
    elif p == 5:
        sa = input_positif("MASUKKAN SISI ATAS: ")
        sb = input_positif("MASUKKAN SISI BAWAH: ")
        t = input_positif("MASUKKAN TINGGI: ")
        luas = (sa + sb) * t * 0.5
        nama = "TRAPESIUM"
    elif p == 6:
        d1 = input_positif("MASUKKAN DIAGONAL 1: ")
        d2 = input_positif("MASUKKAN DIAGONAL 2: ")
        luas = d1 * d2 * 0.5
        nama = "BELAH KETUPAT"
    elif p == 7:
        d1 = input_positif("MASUKKAN DIAGONAL 1: ")
        d2 = input_positif("MASUKKAN DIAGONAL 2: ")
        luas = d1 * d2 * 0.5
        nama = "LAYANG - LAYANG"
    elif p == 8:
        r = input_positif("MASUKKAN JARI - JARI: ")
        luas = 0.5 * math.pi * r * r
        nama = "SETENGAH LINGKARAN"
    elif p == 9:
        s = input_positif("MASUKKAN SISI: ")
        luas = (3 * math.sqrt(3) * s * s) / 2
        nama = "SEGI ENAM BERATURAN"
    elif p == 10:
        a = input_positif("MASUKKAN ALAS: ")
        t = input_positif("MASUKKAN TINGGI: ")
        luas = a * t * 0.5
        nama = "SEGITIGA"
    else:
        print("!! PILIHAN TIDAK TERSEDIA !!")
    if nama is not None:
        print(f"Luas {nama} = {luas:.4f}")
        with open("hasil_perhitungan.txt", "a", encoding="utf-8") as f:
            f.write(f"Luas {nama} = {luas:.4f}\n")