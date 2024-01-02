def konversi_jam():
    detik = int(input("detik: "))
    jam = detik // 3600
    sisaJam = detik % 3600
    menit = sisaJam // 60
    sisaMenit = sisaJam % 60
    detik = sisaMenit % 60
    return jam, menit, detik

def tambah_waktu(jam, menit, detik):
    pilihan = int(input("Jenis waktu yang ingin ditambahkan (1. detik 2. menit 3. jam):"))
    if pilihan == 1:
        tambahDetik = int(input("detik: "))
        detik += tambahDetik
        if detik >= 60:
            menit += detik // 60
            detik %= 60
    elif pilihan == 2:
        tambahMenit = int(input("menit: "))
        menit += tambahMenit
        if menit >= 60:
            jam += menit // 60
            menit %= 60
    elif pilihan == 3:
        tambahJam = int(input("jam: "))
        jam += tambahJam
        if jam >= 24:
            jam %= 24
    return jam, menit, detik

def format_waktu(jam, menit, detik):
    if jam < 10:
        jam = f"0{jam}"
    if menit < 10:
        menit = f"0{menit}"
    if detik < 10:
        detik = f"0{detik}"
    print(f"{jam} : {menit} : {detik}")

def main():
    jam, menit, detik = konversi_jam()
    print(f"Waktu sekarang:\n{jam}:{menit}:{detik}")
    jam, menit, detik = tambah_waktu(jam, menit, detik)
    format_waktu(jam, menit, detik)

if __name__ == '__main__':    
    main()   