def main():
    # Deklarasi array
    n = int(input())
    array = [""] * n
    # Input array
    for i in range(0, n, 1):
        array[i] = input()
    # Kata yang dicari
    cari = str(input("cari: "))
    print(f"judul yang mengandung kata {cari}:")
    for i in range(0, n, 1):
        if (cari in array[i]):
            print(array[i])


if __name__ == '__main__':
    main()
