def cari_nrp(nrp, nama, n, dicari):
    for i in range(0, n, 1):
        nrp[i] = str(input("NRP : "))
        nama[i] = str(input("Nama : "))
    dicari = str(input("NRP yang dicari : "))
    while dicari != "9999":
        ada = False
        for i in range(0, n, 1):
            if dicari == nrp[i]:
                ada = True
                simpanIndex = i
        if ada:
            print(f"Nama dari {dicari} adalah {nama[simpanIndex]}")
        else:
            print("Data NRP yang dicari tidak ditemukan")
        dicari = str(input("NRP yang dicari : "))
    print("Selesaiiiiii")
    return


def main():
    n = int(input("Jumlah data : "))
    nrp = [None] * n
    nama = [None] * n
    cari_nrp(nrp, nama, n, "")


if __name__ == "__main__":
    main()
