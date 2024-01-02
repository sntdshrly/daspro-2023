def daftar_menu():
    daftarMenu = {
        "Solario": {
            "menu_list": {
                1: ("Nasi goreng seafood", 40000),
                2: ("Bihun siram ayam", 37000),
                3: ("Es teh manis", 9000),
            },
            "voucher": {
                "JAYAJAYA": 8000,
            }
        },
        "Tobarob": {
            "menu_list": {
                1: ("Ayam panggang itali", 32000),
                2: ("Dori sambal matah", 30000),
                3: ("Iced rock coffee", 25000),
            },
            "voucher": {
                "FOLLOWYUK": 15000,
            }
        }
    }
    return daftarMenu

def pilih_menu(daftarMenu):
    menuPilih = ""
    harga = 0
    nama = input("Nama pemesan: ")
    print("==========================")
    print("1. Solario\n2. Tobarob")
    tempat = int(input("Silahkan Pilih Tempat: "))

    print("==========================")
    if tempat == 1:
        menuTempat = daftarMenu["Solario"]
        tempat = "Solario"
    elif tempat == 2:
        menuTempat = daftarMenu["Tobarob"]
        tempat = "Tobarob"
    print(f"Selamat datang di {tempat}")
    print("1. Pesan\n2. Cetak Struk")
    pilihan = int(input("Pilihan: "))

    while pilihan != 2:
        print("======= Menu =======")
        for key, value in menuTempat["menu_list"].items():
            print(f"{key}. {value[0]}")

        menu = int(input("Silahkan pilih menu: "))
        selected_menu = menuTempat["menu_list"].get(menu)
        if selected_menu:
            if menuPilih:
                menuPilih += ','
            menuPilih += f' {selected_menu[0]}'
            harga += selected_menu[1]
            print("Menu ditambahkan")

        print("1. Pesan\n2. Cetak Struk")
        pilihan = int(input("Pilihan: "))

    print("==========================")
    voucher = input("Masukkan kode voucher\n")
    potongan = menuTempat["voucher"].get(voucher, 0)

    if potongan > 0:
        print("Kode voucher benar !!")
    else:
        print("Kode voucher salah !!")

    print(f"==== Pesanan {tempat} ====\nNama: {nama}\nPesanan: {menuPilih}\nHarga: {harga}\nPPN: {int(harga * 15 / 100)}\nPotongan: {potongan}\nTotal: {int(harga + (harga * 15 / 100) - potongan)}")
    print("==========================")

def main():
    daftarMenu = daftar_menu()
    pilih_menu(daftarMenu)


if __name__ == '__main__':
    main()
