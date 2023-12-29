def main():
    status = 1
    n = int(input())
    for i in range(2, n, 1):
        if (n % i == 0):
            status = 0
    if (status == 1 and n > 1):
        print("prima")
    else:
        print("bukan prima")


if __name__ == '__main__':
    main()
