def ganjil(z):
    for i in range(0, z + 2, 2):
        for _ in range(z, i, -2):
            print(" ", end=" ")
        for _ in range(0, i - 1, 1):
            print("*", end=" ")
        for _ in range(z, i, -2):
            print("   ", end=" ")
        for _ in range(0, i - 1, 1):
            print("*", end=" ")
        print()


def genap(z):
    for i in range(0, z + 2, 2):
        for _ in range(z, i, -2):
            print(" ", end=" ")
        for _ in range(0, i, 1):
            print("*", end=" ")
        for _ in range(z, i, -2):
            print("  ", end="  ")
        for _ in range(0, i, 1):
            print("*", end=" ")
        print()


def bawah(z):
    for i in range(z, 0, -1):
        print("  " * (z - i), end="")
        print(" * *" * i, end=" ")
        print()


def main():
    z = int(input())
    if (z % 2 == 0):
        genap(z)
    else:
        ganjil(z)
    bawah(z)


if __name__ == '__main__':
    main()
