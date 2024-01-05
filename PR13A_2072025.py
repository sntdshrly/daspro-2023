def input_array(n):
    array = [None] * n
    for i in range(0, n, 1):
        array[i] = int(input())
    return array


def simple_sort(n, array):
    for i in range(n - 1):
        imin = i
        for j in range(i + 1, n):
            if array[j] < array[imin]:
                imin = j
        array[i], array[imin] = array[imin], array[i]
    print(*array, end = " ")


def main():
    n = int(input())
    array = input_array(n)
    simple_sort(n, array)


if __name__ == "__main__":
    main()
