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
    digit = str(input("5 digit angka: "))
    while (digit != "99999"):
        listAngka.append(digit)
        i = i + 1
        digit = str(input("5 digit angka: "))
    return listAngka

def cari_kata(arrKata, arrDigitAngka):
    listHasil = []
    print("Kata yang telah dibuat:")
    for i in range(0, len(arrDigitAngka), 1):
        tempString = ""  # Digunakan untuk menampung satu kata
        data = arrDigitAngka[i]
        for j in range(0, len(data), 1):
            tempString += (arrKata[int(data[j])])
        listHasil.append(tempString)
    return listHasil

def tampil_hasil(listHasil):
    for i in range(0, len(listHasil), 1):
        if i == len(listHasil) - 1:
            print(listHasil[i])
        else:
            print(listHasil[i], end=", ")

def main():
    array = input_array()
    listAngka = input_angka()
    listHasil = cari_kata(array, listAngka)
    tampil_hasil(listHasil)

if __name__ == '__main__':
    main()
