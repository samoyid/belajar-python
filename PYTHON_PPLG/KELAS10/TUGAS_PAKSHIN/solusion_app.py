print("                               ")
print("= = = DAFTAR MENU MINUMAN = = =")
print("1. ES TEH  = Rp 5.000")
print("2. KOPI    = Rp 7.000")
print("3. JUS     = Rp 10.000")

while True:
    pilihan = int(input("PILIH MENU (1-3): "))
    if pilihan == 1:
        nama_minuman = "ES TEH"
        harga = 5000
    elif pilihan == 2:
        nama_minuman = "KOPI"
        harga = 7000
    elif pilihan == 3:
        nama_minuman = "JUS"
        harga = 10000
    elif pilihan == 12:
        nama_minuman = "ES TEH & KOPI"
        harga = 12000
    elif pilihan == 21:
        nama_minuman = "ES TEH & KOPI"
        harga = 12000
    elif pilihan == 13:
        nama_minuman = "ES TEH & JUS"
        harga = 15000
    elif pilihan == 31:
        nama_minuman = "ES TEH & JUS"
        harga = 15000
    elif pilihan == 23:
        nama_minuman = "KOPI & JUS"
        harga = 17000
    elif pilihan == 32:
        nama_minuman = "KOPI & JUS"
        harga = 17000
    elif pilihan == 123:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    elif pilihan == 231:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    elif pilihan == 321:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    elif  pilihan == 312:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    elif  pilihan == 132:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    elif  pilihan == 321:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    elif  pilihan == 213:
        nama_minuman = "ES TEH & KOPI & JUS"
        harga = 22000
    else:
        print("!! TIDAK ADA DI DAFTAR MENU !!")
        exit() 

    pajak = harga * 0.02

    total = harga + pajak

    print("                           ")
    print("= = = STRUK PEMBELIAN = = =")
    print("NAMA PESANAN     =", nama_minuman)
    print("HARGA PESANAN    = Rp", harga)
    print("PAJAK 2%         = Rp", int(pajak))
    print("TOTAL PEMBAYARAN = Rp", int(total))