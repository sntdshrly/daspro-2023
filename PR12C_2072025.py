def deklarasi_matriks(d1, d2):
    array = [None] * d1
    for i in range(d1):
        array[i] = [None] * d2
    return array


def input_matriks(d1, d2):
    matriks = deklarasi_matriks(d1, d2)
    # Matriks
    for i in range(d1):
        for j in range(d2):
            matriks[i][j] = int(input(f"Posisi [{i}][{j}]: "))
    return matriks


def hitung_angka_satu(matriks, baris, kolom):
    totalAngkaSatu = 0
    # Posisi sekarang yaitu matriks[baris][kolom]
    barisMatriks = len(matriks)
    kolomMatriks = len(matriks[0])
    # Cek ke kiri
    if kolom > 0:
        totalAngkaSatu += matriks[baris][kolom - 1]
    # Cek ke kanan
    if kolom < kolomMatriks - 1:
        totalAngkaSatu += matriks[baris][kolom + 1]
    # Cek ke atas
    if baris > 0:
        totalAngkaSatu += matriks[baris - 1][kolom]
    # Cek ke bawah
    if baris < barisMatriks - 1:
        totalAngkaSatu += matriks[baris + 1][kolom]
    # Cek diagonal kiri atas
    if baris > 0 and kolom > 0:
        totalAngkaSatu += matriks[baris - 1][kolom - 1]
    # Cek diagonal kanan atas
    if baris > 0 and kolom < kolomMatriks - 1:
        totalAngkaSatu += matriks[baris - 1][kolom + 1]
    # Cek diagonal kiri bawah
    if baris < barisMatriks - 1 and kolom > 0:
        totalAngkaSatu += matriks[baris + 1][kolom - 1]
    # Cek diagonal kanan bawah
    if baris < barisMatriks - 1 and kolom < kolomMatriks - 1:
        totalAngkaSatu += matriks[baris + 1][kolom + 1]
    return totalAngkaSatu


def minesweeper(matriks):
    barisMatriks = len(matriks)
    kolomMatriks = len(matriks[0])
    outputMatriks = deklarasi_matriks(barisMatriks, kolomMatriks)
    for baris in range(barisMatriks):
        for kolom in range(kolomMatriks):
            outputMatriks[baris][kolom] = hitung_angka_satu(
                matriks, baris, kolom)
    return outputMatriks


def main():
    N = int(input("n: "))
    matriks = input_matriks(N, N)
    hasilMatriks = minesweeper(matriks)
    for baris in hasilMatriks:
        print(" ".join(map(str, baris)))


if __name__ == '__main__':
    main()
