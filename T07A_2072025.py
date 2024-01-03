def deret_ganjil(n):
    i = 1
    while i <= n * 2:
        print(i, end=" ")
        i += 2


def deret_genap(n):
    i = 2
    while i <= n * 2:
        print(i, end=" ")
        i += 2


def main():
    n = int(input())
    if n % 2 == 0:
        deret_ganjil(n)
    elif n % 2 == 1:
        deret_genap(n)


if __name__ == '__main__':
    main()
