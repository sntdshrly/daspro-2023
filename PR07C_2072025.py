def is_palindrome(x):
    if (x % 11 == 0) and (x != 110):
        print (f"{x} adalah bilangan palindrom")
    else:
        print (f"{x} bukan bilangan palindrom") 

def is_square(x):
    if x < 0:
        print(f"{x} bukan bilangan kuadrat")
    elif x == 0 or x == 1:
        print(f"{x} adalah kuadrat dengan akar {x}")
    else:
        # Ambil akar dari x
        a = int(x ** 0.5)
        if a * a == x:
            print(f"{x} adalah kuadrat dengan akar {a}")
        else:
            print(f"{x} bukan bilangan kuadrat")

def is_convert_binary(x):
    tempList = []
    while x > 0:
        tempList.insert(0, x % 2)
        x //= 2
    listBiner = []
    listBiner.extend(tempList)
    if len(listBiner) < 9:
        listBiner = [0] * (8 - len(listBiner)) + listBiner
    print(*listBiner, sep = " ")

def main():
    n = 0
    while n != 999:
        n = int(input("N: "))
        if n == 999:
            print("Program selesai")
        if n < 0 or n >= 129:
            print("Angka harus 0 < x < 129")
        else:
            is_palindrome(n)
            is_square(n)
            is_convert_binary(n)

if __name__ == '__main__':
    main()
