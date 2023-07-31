# Python program for implementation of Bubble Sort

def nathan_bubbleSort(item):
    n = len(item)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if item[j] > item[j + 1]:
                swapped = True
                item[j], item[j + 1] = item[j + 1], item[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


# Driver code to test above
item = [64, 34, 25, 12, 22, 11, 90]

nathan_bubbleSort(item)

print("Sorted array is:")
for i in range(len(item)):
    print("% d" % item[i], end=" ")
