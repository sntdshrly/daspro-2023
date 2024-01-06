def input_array(n):
    array = [None] * n
    for i in range(0, n, 1):
        array[i] = int(input())
    return array

def sequential_search(n, cari, array):
    i = 0
    while i < n and array[i] != cari:
        i += 1
    if i < n:
        return i
    else:
        return False

def tampil(indexCari, cari):
    if indexCari:
        print(f"Angka {cari} ditemukan pada indeks ke-{indexCari}.")
    else:
        print(f"Angka {cari} tidak ditemukan.")

def main():
    n = int(input("N : "))
    array = input_array(n)
    cari = int(input("Angka yang dicari: "))
    indexCari = sequential_search(n, cari, array)
    tampil(n, indexCari, cari)


if __name__ == '__main__':
    main()