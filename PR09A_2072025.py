def main():
    n = int(input())
    array = list(map(int, input().split()))
    minimum = array[0]
    for i in range(1, n, 1):
        if (array[i] < minimum):
            minimum = array[i]
    minimum2 = float('inf')
    for i in range(0, n, 1):
        if (array[i] != minimum) and (array[i] < minimum2):
            minimum2 = array[i]
    print(minimum2)


if __name__ == '__main__':
    main()
