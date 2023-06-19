def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2
  # Проверяем существует ли левый элемент больше корня
    if l < n and arr[i] < arr[l]:
        largest = l
# Cуществует ли правый элемент больше корня
    if r < n and arr[largest] < arr[r]:
        largest = r
# Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап
# Применяем heapify к корню.
        heapify(arr, n, largest)

# Сортировка массива заданного размера
def heapSort(arr):
    n = len(arr)
    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # меняем местами
        heapify(arr, i, 0)
    return arr

# Управляющий код для тестирования
arr = list(map(int,input().split())) # Через побел вводим значения элементов массива

print("Sorted array is", *heapSort(arr))