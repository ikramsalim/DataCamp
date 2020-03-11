"""
Convert the code on the right to a one-liner that calculates the variable sel as before.
"""
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]
#sel = cars[dr]

# Print sel
print(sel)