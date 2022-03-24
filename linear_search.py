def linear_search(arr,search_item):
    low = 0
    search_result = False

    while low < len(arr) and not search_result:
        if arr[low] == search_item:
            search_result = True
        else:
            low += 1

    return search_result

lst = [34,2,34,7,87,45,12,43]
value = int(input('Ведите искомый элемент:'))
result = linear_search(lst,value)
if result:
    print('Элемент найден!')
else:
    print('Такого элемента нет!')