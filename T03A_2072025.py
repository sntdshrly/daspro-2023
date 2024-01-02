def input_data():
    bagian, nomor, nama, status, golongan, jam = (
        str(input("Bagian Karyawan : ")),
        int(input("Nomor : ")),
        str(input("Nama : ")),
        str(input("Status Nikah : ")),
        int(input("Golongan : ")),
        int(input("Jam Kerja : "))
    )
    return bagian, nomor, nama, status, golongan, jam


def syarat(bagian, nomor, nama, status, golongan, jam):
    # Bagian
    if (bagian == "Ketua" or bagian == "ketua"):
        bagian = "K"
    elif (bagian == "Staff" or bagian == "staff"):
        bagian = "S"

    # Golongan
    if (golongan == 1):
        gajiPokok = 5000000
    elif (golongan == 2):
        gajiPokok = 3500000
    elif (golongan == 3):
        gajiPokok = 2500000

    # Tunjangan
    if (status == "Ya" or status =="ya"):
        anak = int(input("Jumlah Anak : "))
        tunjangan = 500000 + (gajiPokok * 10 / 100) * anak
        gaji = gajiPokok + tunjangan
    elif (status == "Tidak" or status == "tidak"):
        tunjangan = 300000
        gaji = gajiPokok + tunjangan

    # Bonus
    if (jam > 160):
        bonus = 15000 * (jam - 160)
        gaji = gaji + bonus
    else:
        bonus = 0
        gaji = gaji + bonus
    return bagian, nomor, nama, status, golongan, jam, gajiPokok, tunjangan, bonus, gaji


def print_data(bagian, nomor, nama, status, golongan, jam, gajiPokok, tunjangan, bonus, gaji):
    print("===========================")
    print(f"NIP : {bagian}_{nomor} - {nama}\nGaji Pokok : {gajiPokok:.0f}\ntunjanganangan : {tunjangan:.0f}\nGaji Tambahan : {bonus:.0f}\nTotal Gaji : {gaji:.0f}")


def main():
    bagian, nomor, nama, status, golongan, jam = input_data()
    bagian, nomor, nama, status, golongan, jam, gajiPokok, tunjangan, bonus, gaji = syarat(bagian, nomor, nama, status, golongan, jam)
    print_data(bagian, nomor, nama, status, golongan, jam, gajiPokok, tunjangan, bonus, gaji)


if __name__ == '__main__':
    main()
