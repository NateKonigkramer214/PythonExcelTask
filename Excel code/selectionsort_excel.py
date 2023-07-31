import pandas as pd
#CSV Function
def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe
#Sort Function
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the minimum value is the first element in the unsorted part
        min_index = i

        # Find the minimum value's index in the unsorted part
        for j in range(i + 1, n):
            if arr[j]['Price'] < arr[min_index]['Price']:
                min_index = j

        # Swap the minimum value with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Vars
columns = [0, 4]
filepath = 'D:\Python_Excel_Task\DiamondValues.csv'
dataframe = read_csv(filepath, columns)
# Print the original CSV data
print("CSV Data: ")
print(dataframe)
print("")
# Convert DataFrame to list of dictionaries to perform selection sort
data_list = dataframe.to_dict('records')
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
