def binary_search(list1,key):
    First = 0
    Last = len(list1) - 1
    while First <= Last:
        midle = (First + Last)//2
        if list1[midle] == key:
            return f'Искомый элемент находится под индексом: {midle}'
        elif list1[midle] > key:
            Last = midle - 1
        elif list1[midle] < key:
            First = midle + 1
    return f'Элемент не найден'

N = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


print(N)
print(binary_search(N,16))

