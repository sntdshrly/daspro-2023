def operator_tambah(a, b):
    print("Perhitungan: ")
    print(a,"+",b,"=",a+b)

def operator_kurang(a, b):
    print("Perhitungan: ")
    print(a,"-",b,"=",a-b)

def operator_kali(a, b):
    print("Perhitungan: ")
    print(a,"*",b,"=",a*b)

def operator_bagi(a, b):
    print("Perhitungan: ")
    print(a,"/",b,"=",a/b)

def operator_mod(a, b):
    print("Perhitungan: ")
    print(a,"%",b,"=",a%b)

def operator_pangkat(a, b):
    print("Perhitungan: ")
    print(a,"^",b,"=",a**b)


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = input("c: ")
    if c == "+":
        operator_tambah(a, b)
    elif c == "-":
        operator_kurang(a, b)
    elif c == "*":
        operator_kali(a, b)
    elif c == "/":
        operator_bagi(a, b)
    elif c == "%":
        operator_mod(a, b)
    elif c == "^":
        operator_pangkat(a, b)


if __name__ == '__main__':
    main()
