import pandas as pd
#CSV Function
def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe
#Sort Function
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Vars
columns = [0, 4]
filepath = 'D:\Python_Excel_Task\DiamondValues.csv'
dataframe = read_csv(filepath, columns)
# Print the original CSV data
print("CSV Data: ")
print(dataframe)
print("")
column = "Price"
# Convert DataFrame column to a list
data_list = dataframe[column].tolist()
print("Data List: ")
print(data_list)
# Sort the data using selection sort based on the 'Price' column
selection_sort(data_list)
print(" ")
# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)
# Print the sorted DataFrame
print("Selection Sorted Data:")
print(sorted_dataframe)
