def dataIpsSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


data_array = [3.8, 2.9, 3.3, 4.0, 2.4]

print(f"Data mahasiswa dari yang terbesar hingga terkecil: {dataIpsSort(data_array)}")