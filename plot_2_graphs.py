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

#Graph 1 Unsorted data
plt.subplot(1, 2, 1) 
plt.plot(dataframe, color = "orange")
plt.ylabel('Price')
plt.xlabel("Carat")
plt.title("Graph showing unsorted data")
plt.subplot(1, 2, 2) 
#Graph 2 Sorted data: 
plt.plot(sorted_dataframe, color = "red")
plt.ylabel('Price')
plt.xlabel("Carat")
plt.title("Graph showing sorted data")

plt.legend()
plt.show()
