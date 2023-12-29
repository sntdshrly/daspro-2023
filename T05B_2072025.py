def main():
    kalimat = ""
    karakter = input("Karakter: ")[0]
    kalimat += karakter
    while karakter != ".":
        karakter = input("Karakter: ")[0]
        kalimat += karakter
    print("Hasil Kalimat: ")
    print(''.join(kalimat))

if __name__ == '__main__':
    main()