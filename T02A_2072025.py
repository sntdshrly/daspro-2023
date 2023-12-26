def main():
    uang = {
        'Euro': 16205,
        'Peso': 275.84,
        'Won': 11.69
    }
    jumlah, mataUang = (
        float(input("Jumlah Rupiah: Rp ")),
        str(input("Mata uang(Euro/Peso/Won): ")))
    print("=========================")
    if mataUang in uang:
        print(
            f"{jumlah:.0f} Rupiah sama dengan {(jumlah / uang[mataUang]):.2f} {mataUang} ")
    else:
        print(f"Mohon maaf mata uang {mataUang} tidak dikenali")


if __name__ == '__main__':
    main()
