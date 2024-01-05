def input_array(n):
    array = [None] * n
    for i in range(n):
        array[i] = int(input())
    return array


def iris(n, array1, array2):
    hasil = []
    for i in range(n):
        if array1[i] in array2 and array1[i] not in hasil:
            hasil.append(array1[i])
    print("Hasil irisan:", end=" ")
    for elemen in hasil:
        print(elemen, end=" ")


def main():
    n = int(input("N: "))
    array1 = input_array(n)
    m = int(input("M: "))
    array2 = input_array(m)
    iris(n, array1, array2)


if __name__ == "__main__":
    main()
