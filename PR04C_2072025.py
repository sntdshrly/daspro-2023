def main():
    dataPenumpang = []
    totalTempuh = 0
    dekat = float('inf')
    jauh = float('-inf')
    jumlahPenumpang = int(input("Jumlah Penumpang : "))
    print("====================================")
    for _ in range(jumlahPenumpang):
        nama, tujuan, jarakTempuh = (
            str(input("Nama : ")),
            str(input("Tujuan : ")),
            float(input("Jarak tempuh (km) : "))
        )
        print("====================================")
        dataPenumpang.append((nama, tujuan, jarakTempuh))
        totalTempuh += jarakTempuh
        if (jarakTempuh < dekat):
            dekat = jarakTempuh
            ruteTerdekat = tujuan
        if (jarakTempuh > jauh):
            jauh = jarakTempuh
            ruteTerjauh = tujuan
    
    print("SUMMARY HARI INI\n====================================")
    print("Total Customer :", jumlahPenumpang)
    print()
    print("Rute Hari ini :")
    for nama, tujuan, jarakTempuh in dataPenumpang:
        print("|", tujuan, end=" ")
    print()
    print("====================================")
    print(f"Total jarak perjalanan hari ini : {totalTempuh:.2f}")
    print("Perjalanan dengan jarak terdekat :", dekat, "menuju", ruteTerdekat)
    print("Perjalanan dengan jarak terjauh :", jauh, "menuju", ruteTerjauh)


if __name__ == '__main__':
    main()
