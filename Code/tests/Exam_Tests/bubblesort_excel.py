import pandas as pd

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n -i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr 


def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe


columns = [0,4]

filepath = 'D:\Python_Excel_Task\DiamondValues.csv'

dataframe = read_csv(filepath, columns)

print("CSV Data: ")
print(dataframe)
print("")

column = "Price"
data_list = dataframe[column].tolist()

print(" ")
print(data_list)
print(" ")

bubble_sort(data_list)

sorted_dataframe = pd.DataFrame(data_list)
print("Bubble Sorted Data:")
print(sorted_dataframe)