# Selection sort in Python


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the minimum value is the first element in the unsorted part
        min_index = i

        # Find the minimum value's index in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum value with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]


data = [-2, 45, 0, 11, -9]
selection_sort(data)
print('Sorted Array in Ascending Order:')
print(data)