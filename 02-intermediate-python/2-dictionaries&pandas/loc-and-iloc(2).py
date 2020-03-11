"""
Print out the drives_right value of the row corresponding
to Morocco (its row label is MOR)
Print out a sub-DataFrame, containing the observations
for Russia and Morocco and the columns country and drives_right.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'], [ 'country', 'drives_right']])


#RUN THE CODE BELOW IN THE IPython Shell
# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]
#
# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]
#
# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]
