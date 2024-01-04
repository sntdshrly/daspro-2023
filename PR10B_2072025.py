def cek_vokal(n):
    arrayNama = [None] * n
    simpanNama = []

    for i in range(n):
        arrayNama[i] = str(input())

    listVokal = ['a', 'i', 'u', 'e', 'o']

    for nama in arrayNama:
        if nama.split()[0][0].lower() in listVokal:
            simpanNama.append(nama)
    return simpanNama


def cek_umur(simpanNama):
    simpanNama = [nama for nama in simpanNama if int(nama.split()[1]) >= 17]

    for nama in simpanNama:
        print(nama.split()[0])


def main():
    n = int(input())
    simpanNama = cek_vokal(n)
    cek_umur(simpanNama)


if __name__ == '__main__':
    main()
