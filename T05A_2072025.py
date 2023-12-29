def main():
    listBilangan = []
    bilangan = int(input())
    while bilangan != 9999:
        listBilangan.append(bilangan)
        bilangan = int(input())
    print(f"Jumlah Angka: {len(listBilangan)}")
    print(f"Total Angka: {sum(listBilangan)}")
    print(f"Rata-rata: {sum(listBilangan)/len(listBilangan):.0f}")

if __name__ == '__main__':
    main()
