def main():
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
        100: 'seratus'
    }
    angka = int(input("Angka: "))
    print("Hasil konversi:")
    if angka in dictAngka:
        print(dictAngka[angka])
    else:
        if 20 < angka < 100:
            puluhan = angka // 10 * 10
            satuan = angka % 10
            if satuan == 0:
                print(dictAngka[puluhan])
            else:
                print(dictAngka[puluhan] + " " + dictAngka[satuan])


if __name__ == '__main__':
    main()
