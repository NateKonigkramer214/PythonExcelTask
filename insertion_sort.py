import pandas as pd

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Store the current dictionary to be inserted
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key['Price'] to one position ahead of their current position
        while j >= 0 and key['Price'] < arr[j]['Price']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the current dictionary at the correct position

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

# Convert DataFrame to list of dictionaries to perform bubble sort
data_list = dataframe.to_dict('records')

# Sort the data using bubble sort based on the 'Price' column
insertion_sort(data_list)

# Convert the sorted list of dictionaries back to a DataFrame
sorted_dataframe = pd.DataFrame(data_list)

print("Insertion Sort")
print(sorted_dataframe)