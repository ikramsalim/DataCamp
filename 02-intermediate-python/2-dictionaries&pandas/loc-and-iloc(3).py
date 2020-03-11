# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
#Series has one bracket
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
#TWO SQUARE BRACKETS-> COLUMN
print(cars.loc[:, ['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame

print(cars.loc[:, ['cars_per_cap', 'drives_right']])
