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
    kat_weight = int(input("KAT: "))
    uts_weight = int(input("UTS: "))
    uas_weight = int(input("UAS: "))
    kat_weight /= 100
    uts_weight /= 100
    uas_weight /= 100
    return kat_weight, uts_weight, uas_weight


def hitung_bobot(uts, uas, kat, kat_weight, uts_weight, uas_weight):
    total_bobot = kat_weight + uts_weight + uas_weight
    return round((kat * kat_weight + uts * uts_weight + uas * uas_weight) / total_bobot, 2)


def data_rata_rata(A, B, N, kat_weight, uts_weight, uas_weight):
    min_average = float('inf')
    min_student = ""

    for i in range(N):
        kls = A[i][0]
        nm = A[i][1]
        uts = B[i][0]
        uas = B[i][1]
        kat = B[i][2]
        average = hitung_bobot(uts, uas, kat, kat_weight,
                               uts_weight, uas_weight)
        print(f"Kelas {kls} dengan nama {nm} rata-ratanya {average}")
        if average < min_average:
            min_average = average
            min_student = f"{nm} dari kelas {kls}"
    print(
        f"Rata-rata terkecil diperoleh {min_student} dengan nilai {min_average}")
    return


def main():
    N = int(input("Jumlah siswa: "))
    A, B = input_data(N)
    kat_weight, uts_weight, uas_weight = input_persentase()
    data_rata_rata(A, B, N, kat_weight, uts_weight, uas_weight)


if __name__ == '__main__':
    main()
