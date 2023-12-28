def main():
    alpukat, apel, jeruk = (
        int(input("Jumlah Alpukat (kg) : ")),
        int(input("Jumlah Apel (kg) : ")),
        int(input("Jumlah Jeruk (kg) : ")))
    print(f"=====================\nTotal Harga Buah Rp {(40000 * alpukat) + (35000 * apel) + (20000 * jeruk)}")

if __name__ == '__main__':
    main()
