def deklarasi_matriks(d1, d2):
    array = [None] * d1
    for i in range(d1):
        array[i] = [None] * d2
    return array


def input_matriks(d1, d2):
    matrix = deklarasi_matriks(d1, d2)
    for i in range(d1):
        matrix[i] = list(map(int, input().split()))
    return matrix


def count_column(N, matrix):
    print("Column")
    for i in range(N):
        total = 0
        for j in range(N):
            print(matrix[j][i], end=" ")
            if j < N - 1:
                print("+", end=" ")
            else:
                print("=", end=" ")
            total += matrix[j][i]
        print(total)
    return


def main():
    N = int(input("n: "))
    matrix = input_matriks(N, N)
    count_column(N, matrix)


if __name__ == '__main__':
    main()
