def deklarasi_matriks(n):
    array = [None] * n
    for i in range(0, n, 1):
        array[i] = [None] * n
    return array


def input_matriks(n):
    # Jika ganjil dan n > 3
    if (n % 2 != 0) and (n > 3):
        matriks = (deklarasi_matriks(n))
        for i in range(n):
            matriks[i] = list(map(int, input().split()))
        for i in range(n):
            for j in range(n):
                if i in (0, n-1) or j in (0, n-1) or i == j or j == n-i-1:
                    print(matriks[i][j], end=" ")
                else:
                    print("  ", end="")
            print()
    # Jika genap dan n <= 3
    else:
        print("Masukan N harus ganjil dan lebih dari 3!")


def main():
    n = int(input())
    input_matriks(n)


if __name__ == '__main__':
    main()
