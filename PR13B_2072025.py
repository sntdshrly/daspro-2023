def input_array(n):
    array = [None] * n
    for i in range(0, n, 1):
        array[i] = int(input())
    return array


def sorting_naik(n, array):
    for i in range(0, n-1, 1):
        imin = i
        for j in range(i + 1, n, 1):
            if (array[j] < array[imin]):
                imin = j
        array[i], array[imin] = array[imin], array[i]
    print(*array, end = " ")


def sorting_turun(n, array):
    for i in range(0, n - 1, 1):
        imin = i
        for j in range(i + 1, n, 1):
            if (array[j] > array[imin]):
                imin = j
        array[i], array[imin] = array[imin], array[i]
    print(*array, end = " ")


def main():
    n = int(input())
    array = input_array(n)
    jenis = str(input("Jenis Sorting (up: menaik, down: menurun): "))
    if (jenis == "menaik"):
        sorting_naik(n, array)
    elif (jenis == "menurun"):
        sorting_turun(n, array)


if __name__ == "__main__":
    main()
