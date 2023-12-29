def menu_mixu():
    return {
        'Creamy Mango Boba': {
            'Unyu': 20000,
            'Medium': 22000,
            'Large': 24000
        },
        'Boba Sundae': {
            'Unyu': 14000,
            'Medium': 16000,
            'Large': 18000
        },
        'Fresh Squeezed Lemonade': {
            'Unyu': 8000,
            'Medium': 10000,
            'Large': 12000
        }
    }

def menu_moonbucks():
    return {
        'Asian Dolce Latte': {
            'Tall': 53000,
            'Grande': 58000,
            'Venti': 60000
        },
        'Caramel Java Chip': {
            'Tall': 58000,
            'Grande': 63000,
            'Venti': 67000
        },
        'Mango Passion Fruit': {
            'Tall': 45000,
            'Grande': 49000,
            'Venti': 52000
        }
    }

def tampilkan_menu(menu):
    for index, minuman in enumerate(menu.keys(), start=1):
        print(f"{index}. {minuman}")

def tampilkan_ukuran_dan_harga(menu):
    for index, (ukuran, harga) in enumerate(menu.items(), start=1):
        print(f"{index}. {ukuran} - {harga}")

def hitung_total(menu, pilihanMenu, pilihanUkuran, potongan):
    namaMenu = list(menu.keys())[pilihanMenu - 1]
    namaUkuran = list(menu[namaMenu].keys())[pilihanUkuran - 1]
    harga = menu[namaMenu][namaUkuran]
    ppn = int(0.1 * harga)
    total = harga + ppn - potongan
    return namaMenu, namaUkuran, harga, ppn, total

def main():
    namaPemesan = input("Nama pemesan: ")
    print("=======================")
    print("1. Mixu\n2. Moonbucks")
    tempat = int(input("Silahkan Pilih Tempat: "))

    if tempat == 1:
        print("=======================\nSelamat datang di Mixu")
        print("======== Menu =========")
        menuMixu = menu_mixu()
        tampilkan_menu(menuMixu)
        pilihMenu = int(input("Silahkan pilih menu: "))
        print("======== Ukuran ========")
        tampilkan_ukuran_dan_harga(menuMixu[list(menuMixu.keys())[pilihMenu - 1]])
        pilihUkuran = int(input("Mau ukuran apa: "))
        print("=======================")
        voucher = input("Masukkan kode voucher: ")
        potongan = 5000 if voucher == "ILOVEMIXU" else 0
        print("Kode voucher benar !!" if potongan else "Kode voucher salah !!")
        print("===== Pesanan Mixu =====")
        namaMenu, namaUkuran, harga, ppn, total = hitung_total(
            menuMixu, pilihMenu, pilihUkuran, potongan
        )
        print(f"Nama: {namaPemesan}")
        print(f"Pesanan: {namaMenu}")
        print(f"Ukuran: {namaUkuran.capitalize()}")
        print(f"Harga: {harga}")
        print(f"PPN: {ppn}")
        print(f"Potongan: {potongan}")
        print(f"Total: {total}")
        print("=======================")

    elif tempat == 2:
        print("=======================\nSelamat datang di Moonbucks")
        print("======== Menu =========")
        menuMoonbucks = menu_moonbucks()
        tampilkan_menu(menuMoonbucks)
        pilihMenu = int(input("Silahkan pilih menu: "))
        print("======== Ukuran ========")
        tampilkan_ukuran_dan_harga(menuMoonbucks[list(menuMoonbucks.keys())[pilihMenu - 1]])
        pilihUkuran = int(input("Mau ukuran apa: "))
        print("=======================")
        voucher = input("Masukkan kode voucher: ")
        potongan = 20000 if voucher == "MOONBUCKSUWU" else 0
        print("Kode voucher benar !!" if potongan else "Kode voucher salah !!")
        print("===== Pesanan Moonbucks =====")
        namaMenu, namaUkuran, harga, ppn, total = hitung_total(
            menuMoonbucks, pilihMenu, pilihUkuran, potongan
        )
        print(f"Nama: {namaPemesan}")
        print(f"Pesanan: {namaMenu}")
        print(f"Ukuran: {namaUkuran.capitalize()}")
        print(f"Harga: {harga}")
        print(f"PPN: {ppn}")
        print(f"Potongan: {potongan}")
        print(f"Total: {total}")
        print("=======================")

if __name__ == '__main__':
    main()
