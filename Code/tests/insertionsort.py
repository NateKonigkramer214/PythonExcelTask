def insertion_sorting(list_a):
    index_len = range(1, len(list_a))
    for i in index_len:
        val_sort = list_a[i]

        while list_a[i - 1] > val_sort and i > 0:
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1

    return list_a


print(insertion_sorting(
    [54, 71, 34, 21, 28, 10, 38, 81, 91, 47, 27, 11, 9, 67, 99, 66, 18, 14, 98, 58, 22, 100, 38, 71, 18, 94, 66, 88, 77,
     81, 47, 86, 97, 42]))
