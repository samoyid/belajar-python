import math
from datetime import datetime

# ===== FIX COLORAMA (ANTI ERROR) =====
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Dummy:
        def __getattr__(self, name):
            return ""
    Fore = Style = Dummy()

# ================= CLASS =================
class BangunDatar:
    def __init__(self, nama):
        self.nama = nama


class Persegi(BangunDatar):
    def __init__(self, s):
        super().__init__("Persegi")
        self.s = s

    def tampil_rumus(self):
        print(Fore.CYAN + "Rumus: s x s")

    def tampil_pola(self):
        print(Fore.YELLOW + "\nPola:")
        for i in range(5):
            print("*****")

    def hitung_luas(self):
        return self.s * self.s


class Lingkaran(BangunDatar):
    def __init__(self, r):
        super().__init__("Lingkaran")
        self.r = r

    def tampil_rumus(self):
        print(Fore.CYAN + "Rumus: π x r x r")

    def tampil_pola(self):
        print(Fore.YELLOW + "\nPola:")
        print("  ***  ")
        print(" *   * ")
        print(" *   * ")
        print("  ***  ")

    def hitung_luas(self):
        return math.pi * self.r * self.r


class Segitiga(BangunDatar):
    def __init__(self, a, t):
        super().__init__("Segitiga")
        self.a = a
        self.t = t

    def tampil_rumus(self):
        print(Fore.CYAN + "Rumus: 1/2 x alas x tinggi")

    def tampil_pola(self):
        print(Fore.YELLOW + "\nPola:")
        for i in range(1, 6):
            print("*" * i)

    def hitung_luas(self):
        return 0.5 * self.a * self.t


# ================= FUNGSI =================
def input_positif(teks):
    while True:
        try:
            val = float(input(teks))
            if val > 0:
                return val
            print(Fore.RED + "Harus lebih dari 0!")
        except:
            print(Fore.RED + "Input tidak valid!")


def simpan_hasil(nama, luas):
    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("hasil_perhitungan.txt", "a", encoding="utf-8") as f:
        f.write(f"{waktu} | {nama:<10} | {luas:.2f}\n")


def tampil_riwayat():
    print(Fore.GREEN + "\n=== RIWAYAT ===")
    try:
        with open("hasil_perhitungan.txt", "r", encoding="utf-8") as f:
            print("Tanggal & Waktu      | Bangun     | Luas")
            print("-"*50)
            print(f.read())
    except FileNotFoundError:
        print("Belum ada data.")


# ================= PROGRAM UTAMA =================
while True:
    print(Style.BRIGHT + Fore.BLUE + "\n=== PROGRAM LUAS BANGUN DATAR ===")
    print("1. Persegi")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Lihat Riwayat")
    print("0. Keluar")

    try:
        p = int(input("Pilih menu: "))
    except:
        print(Fore.RED + "Harus angka!")
        continue

    if p == 0:
        print(Fore.MAGENTA + "Program selesai!")
        break

    elif p == 1:
        s = input_positif("Masukkan sisi: ")
        bangun = Persegi(s)

    elif p == 2:
        r = input_positif("Masukkan jari-jari: ")
        bangun = Lingkaran(r)

    elif p == 3:
        a = input_positif("Masukkan alas: ")
        t = input_positif("Masukkan tinggi: ")
        bangun = Segitiga(a, t)

    elif p == 4:
        tampil_riwayat()
        continue

    else:
        print(Fore.RED + "Pilihan tidak ada!")
        continue

    print(Fore.GREEN + f"\n=== {bangun.nama.upper()} ===")
    bangun.tampil_rumus()
    bangun.tampil_pola()

    luas = bangun.hitung_luas()
    print(Fore.WHITE + f"\nLuas = {luas:.2f}")

    simpan_hasil(bangun.nama, luas)