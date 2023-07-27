import pandas as pd
import matplotlib.pyplot as plt

#CSV Function
def read_csv(filepath, columns):
    dataframe = pd.read_csv(filepath, usecols=columns)
    return dataframe
#Sort Function
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        
        min_index = i

        
        for j in range(i + 1, n):
            if arr[j]['Price'] < arr[min_index]['Price']:
                min_index = j

        
        arr[i], arr[min_index] = arr[min_index], arr[i]


columns = [0, 4]
filepath = 'D:\Python_Excel_Task\DiamondValues.csv'
dataframe = read_csv(filepath, columns)

print("CSV Data: ")
print(dataframe)
print("")

data_list = dataframe.to_dict('records')
print("Data List: ")
print(data_list)

selection_sort(data_list)
print(" ")

sorted_dataframe = pd.DataFrame(data_list)

print("Selection Sorted Data:")
print(sorted_dataframe)

# Ploting data:

plt.plot(dataframe, color = "orange", label = "Unsorted data")
plt.plot(sorted_dataframe, color = "green", label = "Sorted Data", linestyle = "dashed")

plt.xlabel('Carrot')
plt.ylabel('Price')

plt.title("Graph to show sorted vs unsorted data using slection sort")

# plt.legend()
plt.show()