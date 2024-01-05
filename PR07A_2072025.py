def alphabet_count():
    alphabet = "abcde"
    n = int(input("N: "))
    while n !=0:
        for i in range(n):
            print(alphabet[i % len(alphabet)], end=" ")
        print()
        n = int(input("N: "))
    print("Program selesai")

def main():
    alphabet_count()

if __name__ == '__main__':
    main()
