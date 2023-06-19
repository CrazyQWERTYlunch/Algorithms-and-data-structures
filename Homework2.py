def heapify(arr, n, i):
    largest = i # Инициализация корня дерева
    left = 2 * i + 1
    right = 2 * i + 2
  # Проверяем существует ли левый элемент больше корня
    if left < n and arr[i] < arr[left]:
        largest = left
# Cуществует ли правый элемент больше корня
    if right < n and arr[largest] < arr[right]:
        largest = right
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