def print_binary(bilangan):
    tempList = []
    while bilangan > 0:
        tempList.insert(0, bilangan % 2)
        bilangan //= 2
    listBiner = []
    listBiner.extend(tempList)
    if len(listBiner) < 9:
        listBiner = [0] * (9 - len(listBiner)) + listBiner
    print(*listBiner, sep = " ")


def main():
    bilangan = int(input())
    print_binary(bilangan)


if __name__ == '__main__':
    main()
