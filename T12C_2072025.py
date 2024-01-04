def deklarasi_matriks(d1, d2):
    array = [None] * d1
    for i in range(d1):
        array[i] = [None] * d2
    return array


def input_data(n):
    A = deklarasi_matriks(n, 2)
    B = deklarasi_matriks(n, 3)
    print("=" * 40)
    for i in range(n):
        # Matrix A
        kls = input("Kelas: ")
        nm = input("Nama: ")
        # Matrix B
        ka = int(input("Nilai KAT: "))
        ut = int(input("Nilai UTS: "))
        ua = int(input("Nilai UAS: "))
        # Matrix A
        A[i][0] = kls
        A[i][1] = nm
        # Matrix B
        B[i][0] = ut
        B[i][1] = ua
        B[i][2] = ka
        print("=" * 40)
    return A, B


def input_persentase():
    print("Masukkan Persentase Nilai")
    kat_bobot = int(input("KAT: "))
    uts_bobot = int(input("UTS: "))
    uas_bobot = int(input("UAS: "))
    kat_bobot /= 100
    uts_bobot /= 100
    uas_bobot /= 100
    return kat_bobot, uts_bobot, uas_bobot


def hitung_bobot(uts, uas, kat, kat_bobot, uts_bobot, uas_bobot):
    total_bobot = kat_bobot + uts_bobot + uas_bobot
    return round((kat * kat_bobot + uts * uts_bobot + uas * uas_bobot) / total_bobot, 2)


def data_rata_rata(A, B, N, kat_bobot, uts_bobot, uas_bobot):
    min_avg = float('inf')
    min_student = ""

    for i in range(N):
        kls = A[i][0]
        nm = A[i][1]
        uts = B[i][0]
        uas = B[i][1]
        kat = B[i][2]
        avg = hitung_bobot(uts, uas, kat, kat_bobot,
                               uts_bobot, uas_bobot)
        print(f"Kelas {kls} dengan nama {nm} rata-ratanya {avg}")
        if avg < min_avg:
            min_avg = avg
            min_student = f"{nm} dari kelas {kls}"
    print(
        f"Rata-rata terkecil diperoleh {min_student} dengan nilai {min_avg}")
    return


def main():
    N = int(input("Jumlah siswa: "))
    A, B = input_data(N)
    kat_bobot, uts_bobot, uas_bobot = input_persentase()
    data_rata_rata(A, B, N, kat_bobot, uts_bobot, uas_bobot)


if __name__ == '__main__':
    main()
