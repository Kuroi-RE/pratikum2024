def insertion_sort(array):
    for i in range(1, len(array)):
        item = array[i]
        j = i - 1
        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item
    return array

data_array = [34, 66, 8, 80, 72, 2, 89]

print(insertion_sort(data_array))