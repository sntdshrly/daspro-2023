def diamond_atas(n):
    for i in range(0, n, 1):
        for j in range(n, i, -1):
            print(" ", end=" ")
        for k in range(0, 2*(i+1)-1):
            print("+", end=" ")
        for j in range(i, n):
            print(" ", end=" ")
        print()


def diamond_tengah(n):
    for i in range(0, 2 * n + 1, 1):
        print("+", end=" ")
    print()


def diamond_bawah(n):
    for i in range(n-1, -1, -1):
        for j in range(n, i, -1):
            print(" ", end=" ")
        for k in range(0, 2*(i+1)-1):
            print("+", end=" ")
        for j in range(i, n):
            print(" ", end=" ")
        print()


def main():
    n = int(input())
    diamond_atas(n)
    diamond_tengah(n)
    diamond_bawah(n)


if __name__ == '__main__':
    main()
