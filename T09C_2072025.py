def input_array():
    nMax = 10
    array = nMax * [None]
    # Input kamus / huruf 10 digit
    for i in range(0, nMax, 1):
        array[i] = str(input())
    return array

def input_angka():
    # Input digit / angka
    listAngka = []
    i = 0
    digit = str(input("Digit angka: "))
    listAngka.append(digit)
    return listAngka

def cari_kata(arrKata, arrDigitAngka):
    listHasil = []
    for i in range(0, len(arrDigitAngka), 1):
        tempString = ""  # Digunakan untuk menampung satu kata
        data = arrDigitAngka[i]
        for j in range(0, len(data), 1):
            tempString += (arrKata[int(data[j])])
        listHasil.append(tempString)
    print(f"Kata yang telah dibuat: {listHasil[0]}")


def main():
    array = input_array()
    listAngka = input_angka()
    cari_kata(array, listAngka)

if __name__ == '__main__':
    main()
