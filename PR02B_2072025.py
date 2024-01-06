def main():
    total = 0
    totalBuahAlpukat = 0
    totalBuahApel = 0
    totalBuahJeruk = 0
    for _ in range(3):
        buah = str(input("Buah(Alpukat/Apel/Jeruk) : "))
        jumlah = int(input(f"Jumlah {buah.capitalize()} (kg) : "))
        print("=====================")
        if buah.lower() == "alpukat":
            harga = 40000
            total = total + harga * jumlah
            totalBuahAlpukat = totalBuahAlpukat + jumlah
        elif buah.lower() == "apel":
            harga = 35000
            total = total + harga * jumlah
            totalBuahApel = totalBuahApel + jumlah
        elif buah.lower() == "jeruk":
            harga = 20000
            total = total + harga * jumlah
            totalBuahJeruk = totalBuahJeruk + jumlah
    print(f"""Jumlah Buah Alpukat : {totalBuahAlpukat} kg
Jumlah Buah Apel : {totalBuahApel} kg
Jumlah Buah Jeruk : {totalBuahJeruk} kg
Total Jumlah Buah yaitu {totalBuahAlpukat + totalBuahApel + totalBuahJeruk} kg
Total Harga Buah Rp {total}""")


if __name__ == '__main__':
    main()
