import pandas

def  read_excel(filepath, column):
    dataframe = pandas.read_csv(filepath, usecols = column)
    return dataframe
#Vars
column = [0, 4]
filepath = 'D:\Python_Excel_Task\DiamondValues.csv' 
dataframe = read_excel(filepath, column)
print(dataframe)
