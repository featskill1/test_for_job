def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# QuickSort быстро сортирует массивы чисел за счет того, что он использует стратегию "разделяй и властвуй".
# Для случайного порядка чисел он эффективно разбивает массив на меньшие подмассивы, сортирует их и объединяет обратно.
# Даже когда массив уже частично отсортирован, QuickSort показывает хорошие результаты благодаря
# сбалансированности операций разделения.
