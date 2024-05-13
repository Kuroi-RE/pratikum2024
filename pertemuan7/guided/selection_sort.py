def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

data_array = [99, 30, 27, 4, 3, 20, 25, 67, 10, 7]

print(selection_sort(data_array))