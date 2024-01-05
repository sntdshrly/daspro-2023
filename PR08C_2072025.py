def cek_golongan(golongan):
    gajiPokok = 0
    tunjanganKesehatan = 0
    if golongan == 1:
        gajiPokok = 3500000
        tunjanganKesehatan = 750000
    elif golongan == 2:
        gajiPokok = 3000000
        tunjanganKesehatan = 500000
    elif golongan == 3:
        gajiPokok = 2500000
        tunjanganKesehatan = 400000
    elif golongan == 4:
        gajiPokok = 2000000
        tunjanganKesehatan = 300000
    return gajiPokok, tunjanganKesehatan

def cek_status(gajiPokok, status):
    tunjanganKeluarga = 0
    if status == "k":
        tunjanganKeluarga = gajiPokok * 10 / 100
    return tunjanganKeluarga

def hitung_gaji_kotor(gajiPokok, tunjanganKeluarga, tunjanganKesehatan):
    return gajiPokok + tunjanganKeluarga + tunjanganKesehatan

def hitung_pajak(gajiKotor):
    pajak = 0
    if gajiKotor > 3000000:
        pajak = gajiKotor * 5 / 100
    return pajak

def hitung_gaji_bersih(gajiKotor, pajak):
    return gajiKotor - pajak

def cetak_slip_gaji(nama, gajiPokok, tunjanganKeluarga, tunjanganKesehatan, gajiKotor, pajak, gajiBersih):
    print(f"Nama: {nama}")
    print(f"Gaji Pokok: {gajiPokok}")
    print(f"Tunjangan Kesehatan: {tunjanganKesehatan}")
    print(f"Tunjangan Keluarga: {tunjanganKeluarga}")
    print("======================================")
    print(f"Gaji Kotor: {gajiKotor}")
    print(f"Pajak: {pajak}")
    print(f"Gaji Bersih: {gajiBersih}")
    print("======================================")

def main():
    nama, golongan, status = (
        str(input("Nama: ")),
        int(input("Golongan: ")),
        str(input("Status Nikah: ")
        ))
    print("========================================")
    gajiPokok, tunjanganKesehatan = cek_golongan(golongan)
    tunjanganKeluarga = cek_status(gajiPokok, status)
    gajiKotor = hitung_gaji_kotor(gajiPokok, tunjanganKeluarga, tunjanganKesehatan)
    pajak = hitung_pajak(gajiKotor)
    gajiBersih = hitung_gaji_bersih(gajiKotor, pajak)
    cetak_slip_gaji(nama, gajiPokok, tunjanganKeluarga, tunjanganKesehatan, gajiKotor, pajak, gajiBersih)

if __name__ == '__main__':
    main()
