def cek_bulan(bulan):
    if bulan > 12 or bulan < 1:
        print(
            f"Masukan Salah, Tidak ada bulan {bulan}.")
        return False
    return False

def cek_tanggal(tanggal, bulan, tahun):
    # Februari
    if bulan == 2:
        if tahun % 4 == 0: # Tahun kabisat
            if tanggal > 29 or tanggal < 1:
                print(
                    f"Masukan Salah, Tidak ada tanggal {tanggal}.")
        else:
            if tanggal > 28 or tanggal < 1:
                print(
                    f"Masukan Salah, Tidak ada tanggal {tanggal}.")
            
    # Bulan dengan 30 hari
    if bulan in [4, 6, 9, 11]:
        if tanggal > 30 or tanggal < 1:
            print(
                f"Masukan Salah, Tidak ada tanggal {tanggal}.")
        
    # Bulan dengan 31 hari
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        if tanggal > 31 or tanggal < 1:
            print(
                f"Masukan Salah, Tidak ada tanggal {tanggal}.")
    return False

def cek_tahun(tahun):
    # Cek tahun
    if tahun < 0:
        print(
            f"Masukan Salah, Tidak ada tahun {tahun}.")
    return False

def konversi_bulan(tanggal, bulan, tahun):
    bulan_dict = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }
    if bulan in bulan_dict:
        hasilKonversi = str(tanggal) + " " + str(bulan_dict[bulan]) + " " + str(tahun)
        return hasilKonversi
    else:
        return None

def main():
    tanggal, bulan, tahun = (
        int(input("Tanggal : ")),
        int(input("Bulan : ")),
        int(input("Tahun : ")),
    )
    cek_bulan(bulan)
    cek_tanggal(tanggal, bulan, tahun)
    cek_tahun(tahun)
    hasilKonversi = konversi_bulan(tanggal, bulan, tahun)
    if cek_bulan != False and cek_tanggal != False and cek_tahun != False and hasilKonversi is not None:
        print(f"{konversi_bulan(tanggal, bulan, tahun)}")

if __name__ == '__main__':
    main()
