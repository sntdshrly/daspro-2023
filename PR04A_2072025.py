def main():
    awal, muncul, increment = (
        int(input("n: ")),
        int(input("m: ")),
        int(input("x: ")))
    tot = 0
    jml = 0
    n = 0
    print(f"Deret {muncul} angka, dimulai dari {awal} dengan kelipatan {increment}.")
    while tot < muncul:
        n = n+1
        if (n < muncul):
            print(awal, end=", ")
        else:
            print(awal, end="")
        jml = jml + awal
        awal += increment
        tot += 1
    print("\nTotal seluruh deret adalah " + str(jml) + ".")
    print(f"Rata-rata deret adalah {jml/muncul:.0f}")


if __name__ == '__main__':
    main()
