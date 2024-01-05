def deklarasi_matriks(d1, d2):
    array = [None] * d1
    for i in range(d1):
        array[i] = [None] * d2
    return array


def input_matriks(d1, d2):
    matriks = deklarasi_matriks(d1, d2)
    for i in range(d1):
        for j in range(d2):
            matriks[i][j] = int(input())
    return matriks

def rotasi(matriks):
    hasil = deklarasi_matriks(len(matriks), len(matriks[0]))
    for i in range(len(matriks)):
        for j in range(len(matriks[0])):
            hasil[j][len(matriks) - 1 - i] = matriks[i][j]
    return hasil

def main():
    N = int(input("n: "))
    matriks = input_matriks(N, N)
    hasil = rotasi(matriks)
    for i in range(len(hasil)):
        print(*hasil[i])


if __name__ == '__main__':
    main()
