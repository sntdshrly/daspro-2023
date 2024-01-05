def cek_prima(bilangan):
    return all(bilangan % i for i in range(2, bilangan))

def main():
    n = int(input("Masukkan bilangan : "))
    count = 0
    listPrima = []
    bilangan = 2
    while count < n:
        if cek_prima(bilangan):
            count += 1
            listPrima.append(bilangan)
        bilangan += 1
    print("=================================")
    strPrima = ' '.join(map(str, listPrima))
    print(f"Bilangan prima yang didapat :\n{strPrima}")


if __name__ == '__main__':
    main()
