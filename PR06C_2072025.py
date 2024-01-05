def main():
    n = int(input())
    for i in range(1, n + 1, 1):
        for _ in range(1, n + 1, 1):
            for j in range(1, n + 1, 1):
                if (i % 2 == 0) and (j != 1) and (j != n):
                    print(" ", end=" ")
                else:
                    print("*", end=" ")
            print(" ", end=" ")
        print()


if __name__ == '__main__':
    main()
