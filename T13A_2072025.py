def input_array(n):
    array = [None] * n
    for i in range(0, n, 1):
        array[i] = int(input())
    return array

def simple_search(array, x):
    for i in range(0, len(array), 1):
        # Kalau ketemu langsung return indeksnya
        if (array[i] == x):
            return i
    # Kalau ga ketemu, return -1
    return -1

def main():
    n = int(input("N : "))
    array = input_array(n)
    cari = int(input())
    hasil = simple_search(array, cari)
    if (hasil == -1):
        print("teu ketemu")
    else:
        print("ketemu")

if __name__ == '__main__':    
    main()   
