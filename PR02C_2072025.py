def main():
    print("===================================================")
    jenis = str(input("Jenis Pakaian(kaos/kemeja/jaket) : "))
    print("===================================================")

    if jenis == "kaos":
        tipe = "Kaos"
        harga = 70000
        bahan = "berwarna"
        jenis = str(input("Warna Kaos(m. maroon, n. navy, dan l. lilac): "))
        jadi = "maroon" if jenis == "m" else "navy" if jenis == "n" else "lilac"

    elif jenis == "kemeja":
        tipe = "Kemeja"
        bahan = "bermotif"
        harga = 100000
        jenis = str(input("Motif Kemeja(k. kotak-kotak, dan p. polos): "))
        jadi = "kotak-kotak" if jenis == "k" else "polos"

    elif jenis == "jaket":
        tipe = "Jaket"
        harga = 150000
        bahan = "berbahan"
        jenis = str(input("Bahan jaket(b. baby terry, d. denim, t. Taslan): "))
        jadi = "baby terry" if jenis == "b" else "denim" if jenis == "d" else "taslan"

    ukuran = str(input("Ukuran Pakaian(s/m/l): "))

    if ukuran == "m":
        harga += harga * 0.2
    elif ukuran == "l":
        harga += harga * 0.4

    print("===================================================")
    print("Barang yang dibeli:")
    print(f"1 {tipe} {bahan} {jadi} berukuran {ukuran}")
    print(f"Harga: Rp. {harga:.0f}")
    print("===================================================")
    uang = int(input("Uang yang dibayarkan: Rp "))

    kembali = uang - harga

    print(f"Kembalian: Rp. {kembali:.0f}")
    print("===================================================")


if __name__ == "__main__":
    main()
