class car:
    def __init__(self, kecepatan, warna, bentuk):
        self.kecepatan = kecepatan
        self.warna = warna
        self.bentuk = bentuk
    def fungsi(self):
        print("berfungsi untuk menjadi kendaraan transportasi yang di gunakan sehari-hari")

ferari = car("1.kecepatannya mencapai 700hp bahkan bisa lebih dari itu","2.rata-rata keluaran ori dari pabrik berwarna merah","3.mobil ini termasuk kategori mobil sport")

print(ferari.kecepatan)
print(ferari.warna)
print(ferari.bentuk)
ferari.fungsi()