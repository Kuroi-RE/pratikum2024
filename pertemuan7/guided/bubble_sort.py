def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1 - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
    
data_array = [20, 4, 29, 34, 89]

print(bubble_sort(data_array))