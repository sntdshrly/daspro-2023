def main():
    petak = int(input("Jumlah petak: "))
    jenis1 = 0
    jenis2 = 0
    jenis3 = 0
    for i in range(3):
        print(f"======= Penanaman ke-{i + 1} =========")
        jenis = int(input("Jenis: "))
        if (jenis == 1):
            jumlah = int(input("Jumlah turnip: "))
            jenis1 = jenis1 + jumlah
        elif (jenis == 2):
            jumlah = int(input("Jumlah cabbage: "))
            jenis2 = jenis2 + jumlah
        elif (jenis == 3):
            jumlah = int(input("Jumlah cucumber: "))
            jenis3 = jenis3 + jumlah
    total1 = jenis1
    total2 = jenis2 * 3
    total3 = jenis3 * 2
    print(
        f"======== Total Penanaman ========\n{jenis1} turnip pada {total1} petak\n{jenis3} cucumber pada {total3} petak\n{jenis2} cabbage pada {total2} petak")
    total = total1 + total2 + total3
    sisa = petak - total
    print(f"Total {total} petak, tersisa {sisa} petak")


if __name__ == "__main__":
    main()
