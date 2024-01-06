def input_data(n):
    A = []
    B = []
    for _ in range(n):
        # Array A
        bilangan = int(input("Array 1: "))
        A.append(bilangan)
    for _ in range(n):
        # Array B
        bilangan = int(input("Array 2: "))
        B.append(bilangan)
    return A, B

def hitung_array(A, B, N):
    C = [0] * N
    for i in range(N):
        C[i] = A[i] + B[i]
    return C

def hitung_total(A, B, N):
    total = 0
    for i in range(N):
        total += A[i] + B[i]
    return total

def main():
    N = int(input("N: "))
    A, B = input_data(N)
    C = hitung_array(A, B, N)
    stringC = ' '.join(map(str, C))
    print(f"{stringC}")
    total = hitung_total(A, B, N)
    print(f"Total {total}")


if __name__ == '__main__':
    main()
