def cek_tengah_genap(n, listBilangan):
    print(f"Tengah: {(listBilangan[int(n/2)-1])} {(listBilangan[int(n/2)])}")

def cek_tengah_ganjil(n, listBilangan):
    print(f"Tengah: {(listBilangan[int(n/2)])}")

def main():
    listBilangan = []
    n = int(input("N: "))
    for i in range(n):
        bilangan = int(input())
        listBilangan.append(bilangan)
    print(f"Pertama: {(listBilangan[0])}")
    print(f"Terakhir: {(listBilangan[n-1])}")
    if n % 2 == 0:
        cek_tengah_genap(n, listBilangan)
    elif n % 2 == 1:
        cek_tengah_ganjil(n, listBilangan)

if __name__ == '__main__':
    main()
