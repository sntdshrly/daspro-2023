def konversi_waktu(jam, menit, detik):
    if jam < 10:
        jam = f"0{jam}"
    if menit < 10:
        menit = f"0{menit}"
    if detik < 10:
        detik = f"0{detik}"
    print(f"{jam} : {menit} : {detik}")

def main():
    detik, menit, jam = (
        int(input("detik: ")),
        int(input("menit: ")),
        int(input("jam: ")))
    konversi_waktu(jam, menit, detik)
    pilihan = ""
    while (pilihan != 4):
        pilihan = int(input("Jenis waktu yang ingin ditambahkan(1.Detik 2. Menit 3. Jam 4. Exit): "))
        if pilihan == 1:
            detik += int(input("detik: "))
            if detik >= 60:
                detik -= 60
                menit += 1
            if menit >= 60:
                menit -= 60
                jam += 1
            if jam >= 24:
                jam -= 24
        elif pilihan == 2:
            menit += int(input("menit: "))
            if menit >= 60:
                menit -= 60
                jam += 1
            if jam >= 24:
                jam -= 24
        elif pilihan == 3:
            jam += int(input("jam: "))
            if jam >= 24:
                jam -= 24
        print("Hasil perjumlahan:")
        konversi_waktu(jam, menit, detik)

if __name__ == '__main__':
    main()
