def selection_sort(array):
    for i in range(len(array)):
        min_value = i
        for j in range(i,len(array)):
            if array[min_value] > array[j]:
                min_value = j

        array[i],array[min_value] = array[min_value],array[i]
    return array

lst = [4,8,1,7,4,9,1,4]
print(f'Исходный массив:{lst}')
result = selection_sort(lst)
print(f'Результат сортировки:{result}')

