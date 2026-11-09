while True:
    print("login")
    username = input("username : ")
    password = input("password : ")

    if username == "admin" and password == "admin1987":
        print("login berhasil")
        break
    else:
        print("username atau password tidak sesuai, silahkan coba lagi")
