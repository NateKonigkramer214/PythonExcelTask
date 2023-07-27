import pandas as pd
import matplotlib.pyplot as plt


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


# Ploting data:

#Graph 1 Unsorted data
plt.subplot(1, 2, 1) 
plt.plot(dataframe, color = "orange")
plt.ylabel('Price')
plt.xlabel("Carat")
plt.title("Graph showing unsorted data")
plt.subplot(1, 2, 2) 
#Graph 2 Sorted data: 
plt.plot(sorted_data, color = "red")
plt.ylabel('Price')
plt.xlabel("Carat")
plt.title("Graph showing sorted data")

plt.legend()
plt.show()
