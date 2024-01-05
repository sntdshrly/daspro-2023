def deklarasi_matriks(d1, d2):
    array = [None] * d1
    for i in range(d1):
        array[i] = [None] * d2
    return array


def input_matriks(d1, d2):
    matriks1 = deklarasi_matriks(d1, d2)
    matriks2 = deklarasi_matriks(d1, d2)
    # Matriks 1
    for i in range(d1):
        for j in range(d2):
            matriks1[i][j] = int(input("Matriks 1: "))
    # Matriks 2
    for i in range(d1):
        for j in range(d2):
            matriks2[i][j] = int(input("Matriks 2: "))
    return matriks1, matriks2

def fusion(matriks1, matriks2):
    hasil = deklarasi_matriks(len(matriks1), len(matriks1[0]))
    for i in range(len(matriks1)):
        for j in range(len(matriks1[0])):
            hasil[i][j] = matriks1[i][j] + matriks2[i][j]
    for i in range(len(hasil)):
        print(*hasil[i])

def main():
    N = int(input("n: "))
    matriks1, matriks2 = input_matriks(N, N)
    fusion(matriks1, matriks2)

if __name__ == '__main__':
    main()