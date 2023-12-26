def main():
    panjang, lebar, tinggi = (
        int(input("panjang(cm): ")),
        int(input("lebar(cm): ")),
        int(input("tinggi(cm): ")))
    keliling = 4 * (panjang + lebar + tinggi)
    luas = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
    volume = panjang * lebar * tinggi
    print(f"keliling = {keliling} cm")
    print(f"luas = {luas} cm^2")
    print(f"volume = {volume} cm^3")


if __name__ == '__main__':
    main()
