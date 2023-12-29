def hitung_total(jumlahSuku, awal, increment, operasi):
    if operasi == "+":
        total = 0
        for i in range(jumlahSuku):
            total += awal + (i * increment)
        statement = "Jumlah Deret: "
    elif operasi == "*":
        total = 1
        for i in range(jumlahSuku):
            total *= awal + (i * increment)
        statement = "Hasil Kali Deret: "
    elif operasi == "/":
        total = awal
        for i in range(1, jumlahSuku):
            total /= awal + (i * increment)
        statement = "Hasil Pembagian Deret: "
    elif operasi == "-":
        total = awal
        for i in range(1, jumlahSuku):
            total -= awal + (i * increment)
        statement = "Hasil Pengurangan Deret: "
    return total, statement


def main():
    jumlahSuku, awal, increment, operasi = (
        int(input("Jumlah Suku: ")),
        int(input("Awal: ")),
        int(input("Increment: ")),
        str(input("Operasi: ")))
    deret = []
    for i in range(jumlahSuku):
        deret.append(awal + (i * increment))

    print("Deret:", end = " ")
    for i, nilai in enumerate(deret):
        if i == jumlahSuku - 1:
            print(nilai, end = "")
        else:
            print(nilai, end = f"{operasi}")
    print()
    total, statement = hitung_total(jumlahSuku, awal, increment, operasi)
    print(f"{statement}{total}")


if __name__ == '__main__':
    main()
