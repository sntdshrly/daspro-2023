def hitung_avg(nilai):
    return round(sum(nilai) / len(nilai), 1)

def print_data(nama, nilai):   
    for elemenNama, elemenNilai in sorted(zip(nama, nilai), key=lambda x: x[1], reverse=True):
        print(f"{elemenNama}\t\t{elemenNilai}")

def main():
    nama = []
    nilai = []
    n = int(input("Jumlah Siswa : "))
    print("=====================")
    for i in range(n):
        nama.append(input("Nama Siswa : "))
        nilai.append(int(input("Nilai : ")))
        print("=====================")
    n = len(nama)

    print_data(nama, nilai)

    # Mencari nilai tertinggi dgn maximum sort
    nilai_terbesar = 0
    index = 0
    for i in range(n):
        rata = round(nilai[i], 2)
        if rata > nilai_terbesar:
            nilai_terbesar = rata
            index = i

    nama_nilai_terbesar = nama[index]
    nilai_avg = hitung_avg(nilai)

    print(f"Nilai terbesar diperoleh {nama_nilai_terbesar}")
    print(f"Nilai rata-rata: {nilai_avg}")

if __name__ == "__main__":
    main()