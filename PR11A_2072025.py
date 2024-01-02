def print_kelipatan_tiga(arr):
    kelipatanTiga = [i for i in arr if i % 3 == 0]
    if kelipatanTiga:
        print("Kelipatan 3 itu ada", end=" ")
        for i in range(len(kelipatanTiga)):
            if i == len(kelipatanTiga) - 1:
                print(kelipatanTiga[i])
            elif i == len(kelipatanTiga) - 2:
                print(kelipatanTiga[i], end=", dan ")
            else:
                print(kelipatanTiga[i], end=", ")


def print_kelipatan_lima(arr):
    kelipatanLima = [i for i in arr if i % 5 == 0]
    if kelipatanLima:
        print("Kelipatan 5 itu ada", end=" ")
        for i in range(len(kelipatanLima)):
            if i == len(kelipatanLima) - 1:
                print(kelipatanLima[i])
            elif i == len(kelipatanLima) - 2:
                print(kelipatanLima[i], end=", dan ")
            else:
                print(kelipatanLima[i], end=", ")


def print_kelipatan_tujuh(arr):
    kelipatanTujuh = [i for i in arr if i % 7 == 0]
    if kelipatanTujuh:
        print("Kelipatan 7 itu ada", end=" ")
        for i in range(len(kelipatanTujuh)):
            if i == len(kelipatanTujuh) - 1:
                print(kelipatanTujuh[i])
            elif i == len(kelipatanTujuh) - 2:
                print(kelipatanTujuh[i], end=", dan ")
            else:
                print(kelipatanTujuh[i], end=", ")


def print_kelipatan_sebelas(arr):
    kelipatanSebelas = [i for i in arr if i % 11 == 0]
    if kelipatanSebelas:
        print("Kelipatan 11 itu ada", end=" ")
        for i in range(len(kelipatanSebelas)):
            if i == len(kelipatanSebelas) - 1:
                print(kelipatanSebelas[i])
            elif i == len(kelipatanSebelas) - 2:
                print(kelipatanSebelas[i], end=", dan ")
            else:
                print(kelipatanSebelas[i], end=", ")


def input_array(n):
    array = list(map(int, input().split()))
    return array


def main():
    n = int(input())
    array = input_array(n)
    print_kelipatan_tiga(array)
    print_kelipatan_lima(array)
    print_kelipatan_tujuh(array)
    print_kelipatan_sebelas(array)


if __name__ == '__main__':
    main()
