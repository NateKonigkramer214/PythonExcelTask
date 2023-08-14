import pandas as pd

#Insertion Sort Generic Function
def insertion_sort(list_a):
    index_len = range(1, len(list_a))
    for i in index_len:
        val_sort = list_a[i]

        while list_a[i - 1] > val_sort and i > 0:
            list_a[i], list_a[i - 1] = list_a[i - 1], list_a[i]
            i = i - 1
    return list_a

#Read CSV function
def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe

# Column names you want to read from the CSV file
columns = [0,4]
filepath = 'D:\Python_Excel_Task\DiamondValues.csv'
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
print("Datalist: ")
print(data_list)
# Sort the data using bubble sort based on the 'Price' column
insertion_sort(data_list)
# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)
print(" ")
print("Insertion Sort")
print(sorted_dataframe)