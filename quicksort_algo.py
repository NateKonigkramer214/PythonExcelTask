def quick_sort(sequence):
    length = len(sequence) #cacl length of sequence
    if length <= 1:
        return sequence #If the length is less than 1 it will return the seq because already sorted
    else: #
        pivot = sequence.pop() # Getting the pivit using .pop fucntion
    #If the length is greater than 1 then the function proceeds with sorting algo
    #Two lists created to store items that are greater than or less than pivit point
    items_greater = []
    items_lower = []

#This function goes through the sequence and compares each element with the pivot. If the element is greater than pivot is
# added to items greater than list and so on vis versa 
    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) #Return the items_lower + pivot + item_higher

print(quick_sort([5,6,7,8,9,8,7,6,5,6,7,8,9,0])) 