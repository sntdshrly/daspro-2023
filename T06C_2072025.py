def main():
    n = int(input("n:"))
    while n != 999:
        status = True
        for i in range(2, n):
            if n % i == 0:
                status = False
                print(f"{n} bukan bilangan prima karena dapat dibagi oleh {i}")
        if status and n > 1:
            print(f"{n} adalah bilangan prima")
        elif status and n == 1:
            print(f"{n} bukan bilangan prima karena 1 bukan bilangan prima")
        elif status and n < 0:
            print(f"{n} bukan bilangan bulat positif")
        n = int(input("n:"))
    print("Program Berhenti!")


if __name__ == '__main__':
    main()
