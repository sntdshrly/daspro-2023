def main():
    n = int(input('n: '))
    count = 0
    n1 = 0
    n2 = 1
    fibonacciList = []
    while count < n:
        fibonacciList.append(n1)
        bilanganTerakhir = n1 + n2
        n1 = n2
        n2 = bilanganTerakhir
        count += 1
        daftarString = [str(angka) for angka in fibonacciList]
    print(' '.join(daftarString))


if __name__ == '__main__':
    main()
