def my_faktorial(i):
    hasil = 1
    for j in range(i, 0, -1):
        hasil *= j
    return hasil


def main():
    a = int(input())
    print("| a   || nilai faktorial \t|")
    for i in range(a, 0, -1):
        print(f"| {i}!  || {my_faktorial(i)} \t\t\t|")


if __name__ == '__main__':
    main()
