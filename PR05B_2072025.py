def segitiga_satu():
    print("  *  ")
    print("* * *")
    print()

def segitiga_dua():
    print("*")
    print("* *")
    print("*")
    print()

def segitiga_tiga():
    print("  *")
    print("* *")
    print("  *")
    print()

def segitiga_empat():
    print("* * *")
    print("  *")
    print()

def main():
    fungsi_segitiga = [segitiga_satu, segitiga_dua, segitiga_tiga, segitiga_empat]
    n = int(input())
    for i in range(n):
        # print(i) # Misal n = 5, maka akan menampilkan 0, 1, 2, 3, 4
        # print(i % len(fungsi_segitiga)) # Misal n = 5, maka akan menampilkan list 0, 1, 2, 3, 0
        fungsi_segitiga[i % len(fungsi_segitiga)]()

if __name__ == '__main__':
    main()
