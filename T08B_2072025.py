def terbesar(a, b, c, d, e):
    maximum = a
    if (b > maximum):
        maximum = b
    if (c > maximum):
        maximum = c
    if (d > maximum):
        maximum = d
    if (e > maximum):
        maximum = e
    print(maximum)


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    terbesar(a, b, c, d, e)


if __name__ == '__main__':
    main()
