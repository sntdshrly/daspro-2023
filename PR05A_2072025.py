def input_karakter():
    kalimat = ""
    karakter = input()[0]
    kalimat += karakter
    while karakter != ".":
        karakter = input()[0]
        kalimat += karakter
    return kalimat


def cek_huruf(arr, n):
    B = [None] * n
    for i in range(0, n, 1):
        if (arr[i] not in B):
            B[i] = arr[i]
    return B


def cek_muncul(arr1, arr2, n):
    hurufVokal = ['a', 'e', 'i', 'o', 'u']
    m = 0
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            if (arr2[i] != None):
                if (arr1[j] == arr2[i] and arr1[j].lower() in hurufVokal):
                    m += 1
        if (arr2[i] != None and arr2[i].lower() in hurufVokal):
            print(f"Huruf {arr2[i]} = {m}")
        m = 0


def main():
    kalimat = input_karakter()
    print(f"Hasil kalimat:\n{kalimat}")
    arrayDua = cek_huruf(kalimat, len(kalimat))
    cek_muncul(kalimat, arrayDua, len(kalimat))


if __name__ == "__main__":
    main()
