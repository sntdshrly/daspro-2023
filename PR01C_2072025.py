def main():
    uang = [
    "seratus ribu",
    "lima puluh ribu",
    "dua puluh ribu",
    "sepuluh ribu",
    "lima ribu",
    "dua ribu",
    "seribu",
    "lima ratus",
    "dua ratus",
    "seratus",
    "lima puluh"
    ]
    nominal = int(input("nominal = "))
    print("menjadi pecahan :")
    bagiAwal = 100000
    for i in range(11):
        kaliDua = nominal // bagiAwal
        modulo = nominal % bagiAwal
        print(int(kaliDua), " lembar uang", uang[i])
        if i == 1:
            bagiAwal = bagiAwal / 2.5
        elif i == 4:
            bagiAwal = bagiAwal / 2.5
        elif i == 7:
            bagiAwal = bagiAwal / 2.5
        else:
            bagiAwal = bagiAwal / 2
        nominal = modulo

    

if __name__=="__main__":
    main()
