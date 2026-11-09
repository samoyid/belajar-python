class Siswa:
    def __init__ (self, nisn, nama, alamat):
        self.nisn = nisn
        self.nama = nama
        self.alamat = alamat

    def kewajiban(self):
        print("Belajar")

dio = Siswa("1234567890", "dio", "malang")
print(dio.nisn)
print(dio.nama)
print(dio.alamat)
dio.kewajiban()