def terjemahkan_angka(angka):
    dictAngka = {
        0: 'nol',
        1: 'satu',
        2: 'dua',
        3: 'tiga',
        4: 'empat',
        5: 'lima',
        6: 'enam',
        7: 'tujuh',
        8: 'delapan',
        9: 'sembilan',
        10: 'sepuluh',
        11: 'sebelas',
        12: 'dua belas',
        13: 'tiga belas',
        14: 'empat belas',
        15: 'lima belas',
        16: 'enam belas',
        17: 'tujuh belas',
        18: 'delapan belas',
        19: 'sembilan belas',
        20: 'dua puluh',
        30: 'tiga puluh',
        40: 'empat puluh',
        50: 'lima puluh',
        60: 'enam puluh',
        70: 'tujuh puluh',
        80: 'delapan puluh',
        90: 'sembilan puluh',
        100: 'seratus',
        200: 'dua ratus',
        300: 'tiga ratus',
        400: 'empat ratus',
        500: 'lima ratus',
        600: 'enam ratus',
        700: 'tujuh ratus',
        800: 'delapan ratus',
        900: 'sembilan ratus',
        1000: 'seribu',
        2000: 'dua ribu',
        3000: 'tiga ribu',
        4000: 'empat ribu',
        5000: 'lima ribu',
        6000: 'enam ribu',
        7000: 'tujuh ribu',
        8000: 'delapan ribu',
        9000: 'sembilan ribu',
        10000: 'sepuluh ribu'
    }

    if 0 <= angka <= 20:
        return dictAngka[angka]
    elif 20 < angka < 100:
        puluhan = angka // 10 * 10
        satuan = angka % 10
        if satuan == 0:
            return dictAngka[puluhan]
        else:
            return dictAngka[puluhan] + " " + dictAngka[satuan]
    elif 100 <= angka < 1000:
        ratusan = angka // 100 * 100
        sisa = angka % 100
        if sisa == 0:
            return dictAngka[ratusan]
        else:
            return dictAngka[ratusan] + " " + terjemahkan_angka(sisa)
    elif 1000 <= angka < 10000:
        ribuan = angka // 1000
        sisa = angka % 1000
        if sisa == 0:
            return dictAngka[ribuan] + " ribu"
        else:
            return dictAngka[ribuan] + " ribu " + terjemahkan_angka(sisa)

def main():
    angka = int(input("Angka: "))
    hasil_terjemahan = terjemahkan_angka(angka)
    print(f"Hasil konversi:\n{hasil_terjemahan}")

if __name__ == '__main__':
    main()
