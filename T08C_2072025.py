def konversi_menit_jam(menit):
    jam = menit // 60
    return jam

def hitung_sisa_menit(menit):
    sisaMenit = menit % 60
    return sisaMenit

def total_tagihan(menit, jam):
    total = jam * 6000 + 1000
    sisa = (menit % 60) * 125
    diskon = (jam - 1) // 3 * 3 * 500
    totalBayar = total + sisa - diskon
    return totalBayar

def tampil(saldo, durasi):
    print("==============================")
    print(f"Total Sewa {konversi_menit_jam(durasi)} jam {hitung_sisa_menit(durasi)} menit")
    print(f"Jumlah Tagihan: {total_tagihan(durasi, konversi_menit_jam(durasi))}")
    print("==============================")
    tagihan = total_tagihan(durasi, konversi_menit_jam(durasi))
    if tagihan <= saldo:
        sisaSaldo = saldo - tagihan
        print("!!! LUNAS !!!")
        print(f"Sisa Saldo: {sisaSaldo}")
        print("==============================")
    else:
        kekuranganPembayaran = tagihan - saldo
        print(f"Kekurangan pembayaran: {kekuranganPembayaran}")
        print("Mohon lakukan isi ulang kepada admin!")


def main():
    print("========= WARNET KUY =========")
    saldo, durasi = (
        int(input("Jumlah saldo : ")),
        int(input("Durasi sewa (menit) : ")))
    tampil(saldo, durasi)

if __name__ == '__main__':
    main()
