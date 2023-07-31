import pandas as pd

# Read CSV file function
def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Quick Sort
def quick_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

# Column names you want to read from the CSV file
columns = [0, 4]

# Escaping the backslashes
filepath = r'D:\Python_Excel_Task\DiamondValues.csv'

# Read the specified columns from the CSV file into a DataFrame
dataframe = read_csv(filepath, columns)

# Print the original CSV data
print("CSV Data: ")
print(dataframe)
print("")

# Defining Column
column = "Price"

# Convert DataFrame column to a list
data_list = dataframe[column].tolist()

# Applying quick sort and printing sorted data
data_list = quick_sort(data_list)
sorted_data = pd.DataFrame(data_list, columns=[column])
print("Quick Sorted Data: ")
print(sorted_data)
