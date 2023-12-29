def main():
    x1, y1, x2, y2 = (
        int(input("titik acuan x: ")),
        int(input("titik acuan y: ")),
        int(input("titik x: ")),
        int(input("titik y: "))
    )
    # Titik 2 sama dengan titik 1 (acuan)
    if x2 == x1 and y2 == y1:
        print(
            f"titik ({x2,y2}) memiliki posisi yang sama dengan titik acuan ({x1,y1})")
        return
    # Titik 2 berada di kiri bawah titik 1 (acuan)
    elif x2 < x1 and y2 < y1:
        print(
            f"titik ({x2,y2}) terletak disebelah kiri bawah titik acuan ({x1,y1})")
    # Titik 2 berada di kanan bawah titik 1 (acuan)
    elif x2 > x1 and y2 < y1:
        print(
            f"titik ({x2,y2}) terletak disebelah kanan bawah titik acuan ({x1,y1})")
    # Titik 2 berada di kiri atas titik 1 (acuan)
    elif x2 < x1 and y2 > y1:
        print(
            f"titik ({x2,y2}) terletak disebelah kiri bawah titik acuan ({x1,y1})")
    # Titik 2 berada di kanan atas titik 1 (acuan)
    elif x2 > x1 and y2 > y1:
        print(
            f"titik ({x2,y2}) terletak disebelah kanan atas titik acuan ({x1,y1})")


if __name__ == '__main__':
    main()
