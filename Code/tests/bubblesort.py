#Python program for implementation of Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr 

# Driver code to test above
item = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(item)

print("Sorted array is:")
for i in range(len(item)):
    print("% d" % item[i], end=" ")
