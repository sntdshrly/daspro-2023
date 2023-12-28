def main():
    angka1, angka2, angka3, operasi1, operasi2 = (
        int(input("angka1: ")),
        int(input("angka2: ")),
        int(input("angka3: ")),
        str(input("operasi1: ")),
        str(input("operasi2: ")))
    if operasi1 in ["+", "-", "*", "/"] and operasi2 in ["+", "-", "*", "/"]:
        result = eval(f"({angka1} {operasi1} {angka2}) {operasi2} {angka3}")
        print(f"({angka1} {operasi1} {angka2}) {operasi2} {angka3} = {result}")
    else:
        print("salah operator nih!")


if __name__ == '__main__':
    main()
