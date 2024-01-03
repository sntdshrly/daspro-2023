def main():
    listBilangan = []
    n = int(input())
    for i in range(n):
        bilangan = int(input())
        listBilangan.append(bilangan)
    for i in range(n - 1, -1, -1):
        print(listBilangan[i], end = ' ')
    print(f"\nTotal {sum(listBilangan)}")

if __name__ == '__main__':
    main()
