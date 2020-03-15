"""
Count the number of stores of each type.
Count the proportion of stores of each type.
Count the number of departments of each type, sorting the counts in descending order.
Count the proportion of departments of each type, sorting the proportions in descending order.
"""
# Count the number of stores of each type
store_counts = stores["type"].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = stores["type"].value_counts(normalize=True)
print(store_props)

# Count the number of departments of each type and sort
dept_counts_sorted = departments["department"].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each type and sort
dept_props_sorted = departments["department"].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

"""
store_counts = stores["type"].value_counts()
store_props = stores["type"].value_counts(normalize=True)
dept_props_sorted = departments["department"].value_counts(sort=True, normalize=True)
"""
