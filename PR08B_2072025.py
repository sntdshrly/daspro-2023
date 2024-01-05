def hitung_bmi(berat, tinggi):
    tinggi = tinggi / 100
    bmi = berat / (tinggi * tinggi)
    return bmi


def cek_status(BMI):
    if BMI < 18.5:
        print("Underweight atau berat badan kurang.")
    elif 18.5 <= BMI <= 22.9:
        print("Berat badan ideal, sangat bagus.")
    elif 23 <= BMI <= 24.9:
        print("Kategori ideal warning, jaga pola makan dan olahraga")
    elif 25 < BMI < 29.9:
        print("Kondisi berat badan memasuki batas obesitas, segera mulai program diet")
    else:
        print("Anda sudah termasuk kategori obesitas")
    return


def main():
    berat, tinggi = (
        int(input("Berat Badan(kg): ")),
        int(input("Tinggi Badan(cm): ")))
    hitung_bmi(berat, tinggi)
    bmi = hitung_bmi(berat, tinggi)
    print("BMI: {bmi:5.5f}".format(bmi = bmi))
    cek_status(bmi)



if __name__ == '__main__':
    main()
