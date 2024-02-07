import pandas as pd

#Defining the data and index for the series

data = [1, 4, 9, 6, 7]
index = ['a', 'x', 'c', '2', 'e']

#creation of pandas series
series = pd.Series(data, index=index)
print(series)
