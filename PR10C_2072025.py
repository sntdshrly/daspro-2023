def array_satu():
   n1 = int(input())
   list1 = list(map(int, input().split()))
   return n1, list1


def array_dua():
   n2 = int(input())
   list2 = list(map(int, input().split()))
   return n2, list2


def array_tiga(list1, list2):
    list3 = list1 + list2
    return list3


def tampil_array(n1, n2, list3):
    hasil = set()
    for i in range(n1 + n2):
        if list3[i] not in hasil:
            hasil.add(list3[i])
            print(list3[i], end=" ")

def main():
    n1, list1 = array_satu()
    n2, list2 = array_dua()
    list3 = array_tiga(list1, list2)
    tampil_array(n1, n2, list3)


if __name__ == "__main__":
    main()
