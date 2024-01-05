def input_array():
    array = [None] * 5
    for i in range(5):
        array[i] = int(input())
    return array


def get_second_min(array):
    minimum1 = min(array)
    minimum2 = float('inf')
    for bilangan in array:
        if bilangan < minimum2 and bilangan != minimum1:
            minimum2 = bilangan
    print(f"Kedua terkecil: {minimum2}")


def main():
    array = input_array()
    get_second_min(array)


if __name__ == '__main__':
    main()
