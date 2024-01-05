def get_min(array):
    minimum = float('inf')
    for bilangan in array:
        if bilangan < minimum:
            minimum = bilangan
    print(minimum)

def main():
    a = int(input())
    b = int(input())
    listBilangan = []
    listBilangan.append(a)
    listBilangan.append(b)
    get_min(listBilangan)

if __name__ == '__main__':
    main()
