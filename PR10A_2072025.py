def input_bilangan(n, array1, array2, array3):
    for i in range(0, n, 1):
        array1[i] = int(input())
    for i in range(0, n, 1):
        array2[i] = int(input())
    for i in range(0, n, 1):
        array3[i] = int(input())
    return array1, array2, array3


def cari_maksimum(n, array1, array2, array3, arrayMaksimum):
    for i in range(0, n, 1):
        maksimum = float('-inf')
        if (array1[i] > maksimum):
            maksimum = array1[i]
        if (array2[i] > maksimum):
            maksimum = array2[i]
        if (array3[i] > maksimum):
            maksimum = array3[i]
        arrayMaksimum[i] = maksimum
    return arrayMaksimum


def tampil_array(n, arrayMaksimum):
    for i in range(0, n, 1):
        print(arrayMaksimum[i], end=" ")


def main():
    n = int(input())
    # Deklarasi array
    array1 = [None] * n
    array2 = [None] * n
    array3 = [None] * n
    arrayMaksimum = [None] * n
    # Input
    array1, array2, array3 = input_bilangan(n, array1, array2, array3)
    # Proses
    arrayMaksimum = cari_maksimum(n, array1, array2, array3, arrayMaksimum)
    # Tampil
    tampil_array(n, arrayMaksimum)


if __name__ == '__main__':
    main()
