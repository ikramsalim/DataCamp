"""
Print the head of the homelessness DataFrame.
"""
# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)


# Print a description of homelessness
print(homelessness.describe())

"""
.head() returns the first few rows (the “head” of the DataFrame).
.info() shows information on each of the columns, such as the data type and number of missing values.
.shape returns the number of rows and columns of the DataFrame.
.describe() calculates a few summary statistics for each column.
"""