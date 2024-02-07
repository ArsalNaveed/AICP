import pandas as pd

#defining the data dictionary with the data given
data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['Rain', 'Sunny', 'Snow', 'Snow', 'Rain', 'Sunny']
}
#defining the alphabetical index
index = ['a', 'b', 'c', 'd', 'e', 'f']

#creation of pandas dataframe
df = pd.DataFrame(data, index=index)

#calculating the mean, maximum and minimum temperatures
temp_mean = df['temperature'].mean()
temp_max = df['temperature'].max()
temp_min = df['temperature'].min()

#printing the calculated mean, max and min temps
print("Mean temperature is :" , temp_mean, "°C")
print("Maximum temperature is :" , temp_max, "°C")
print("Minimum temperature is :" , temp_min, "°C")
