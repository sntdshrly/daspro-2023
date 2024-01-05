def deklarasi_matriks(d1, d2):
    array = [None] * d1
    for i in range(d1):
        array[i] = [None] * d2
    return array


def input_matriks(d1, d2):
    matriks = deklarasi_matriks(d1, d2)
    # Matriks 1
    for i in range(d1):
        for j in range(d2):
            matriks[i][j] = int(input("Matriks 1: "))

def minesweeper(matriks):
    pass

def main():
    N = int(input("n: "))
    matriks = input_matriks(N, N)
    # minesweeper(matriks)

if __name__ == '__main__':
    main()