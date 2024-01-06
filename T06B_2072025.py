def box(n):
    count = 1
    if n < 4:
        for _ in range(n):
            for _ in range(n):
                if count < 10:
                    print(f" {count} ", end="")
                else:
                    print(f"{count} ", end="")
                count += 1
            print()
    
    else:
        for _ in range(n):
            for _ in range(n):
                if count < 10:
                    print(f" 0{count}", end="")
                else:
                    print(f" {count}", end="")
                count += 1
            print()

def main():
    n = int(input())
    box(n)

if __name__ == "__main__":
    main()
