class Buah:
    def __init__ (self, harga, warna, rasa):
        self.harga = harga
        self.warna = warna
        self.rasa = rasa
    
    def fungsi(self):
        print("Dimakan")

mangga = Buah("5000", "hijau", "manis")

print(mangga.harga)
print(mangga.warna)
print(mangga.rasa)
mangga.fungsi()
    