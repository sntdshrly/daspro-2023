def main():
    n = int(input())
    # Input array
    array = list(map(int, input().split()))
    # Inisialisasi array
    hasil = [None] * n # Pertama array hasil masih kosong
    hasil[0] = array[0] # Isi array hasil dengan array[0]
    for i in range(0, n, 1):
        hasil[i] = array[i] + array[i - 1]
    # Print array
    for i in range(0, n, 1):
            print(hasil[i], end=" ")


if __name__ == '__main__':
    main()
