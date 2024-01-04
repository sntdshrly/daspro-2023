def input_array(n):
    array = [None] * n
    for i in range(0, n, 1):
        array[i] = int(input())
    return array


def cek_ganjil_genap(array):
    arrayGanjil = []
    arrayGenap = []
    for elemen in array:
        if elemen % 2 == 1:
            arrayGanjil.append(elemen)
        elif elemen % 2 == 0:
            arrayGenap.append(elemen)
    return arrayGanjil, arrayGenap


def sorting_menurun(array, n):
    for i in range(0, n - 1, 1):
        imin = i
        for j in range(i + 1, n, 1):
            if array[j] > array[imin]:
                imin = j
        array[i], array[imin] = array[imin], array[i]
    return array


def print_array(arrayGanjil, arrayGenap):
    print(f"The Ganjils : {' '.join(map(str, arrayGanjil))}")
    print(f"The Genaps : {' '.join(map(str, arrayGenap))}")


def main():
    n = int(input("N: "))
    array = input_array(n)
    arrayGanjil, arrayGenap = cek_ganjil_genap(array)
    print_array(arrayGanjil, arrayGenap)
    array = sorting_menurun(array, n)
    print("Habis Diurutin: ",end = "")
    for elemen in array:
        print(elemen, end=" ")

if __name__ == "__main__":
    main()
