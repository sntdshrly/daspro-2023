def main():
    awal, muncul, increment = (
        int(input("n: ")),
        int(input("m: ")),
        int(input("x: ")))
    total = 0
    jumlah = 0
    n = 0
    print(f"Deret {muncul} angka, dimulai dari {awal} dengan kelipatan {increment}.")
    while total < muncul:
        n = n + 1
        if (n < muncul):
            print(awal, end=", ")
        else:
            print(awal, end="")
        jumlah = jumlah + awal
        awal += increment
        total += 1
    print("\Total seluruh deret adalah " + str(jumlah) + ".")
    print(f"Rata-rata deret adalah {jumlah/muncul:.0f}")


if __name__ == '__main__':
    main()
