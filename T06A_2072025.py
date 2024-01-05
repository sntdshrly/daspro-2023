def main():
    n = int(input())
    for i in range(0, n, 1):
        for j in range(n-1, i, -1):
            print(" ", end = " ")
        for k in range(-1, i, 1):
            print("* *", end = " ")
        print()

if __name__ == '__main__':
    main()
