def main():
    n = int(input("N: "))
    for _ in range(n):
        bilangan = int(input())
        if (bilangan % 2 == 0):
            print("Genap")
        elif (bilangan % 2 != 0):
            print("Bukan Genap")


if __name__ == '__main__':
    main()
