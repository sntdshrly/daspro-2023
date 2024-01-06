def main():
    n = int(input())
    for i in range(0, n, 1):
        for _ in range(n-1, i, -1):
            print(" ", end = " ")
        for _ in range(-1, i, 1):
            print("* *", end = " ")
        print()

if __name__ == '__main__':
    main()
