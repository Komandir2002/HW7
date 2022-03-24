def buble_sort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

lst = [3,4,8,1,9,3,6]
print(f'Исходный массив:{lst}')
result = buble_sort(lst)
print(f'Результат сортировки:{result}')

# 2 - Вариянт
#
# from random import randint as rd
# n = 10
# array = []
# for i in range(n):
#     array.append(rd(0,200))
# print(f'Не отсортированный массив:{array}')
# count = 0
# for i in range(n-1):
#     for j in range(n - i - 1):
#         if array[j]>array[j+1]:
#             count += 1
#             temp = array[j]
#             array[j] = array[j+1]
#             array[j+1] = temp
# print(f'Отсортированный массив:{array}')
# print(f'Проходов всего:{count}')



