"""
Without an index, subsetting takes the form df[df["column"].isin(values)].
With an index, subsetting takes the form df_ind.loc[values].
"""
"""
Create a list of cities to subset on: Moscow and Saint Petersburg. Assign to cities.
Use [] subsetting to filter temperatures for rows where the city column takes a value in cities.
Use .loc[] subsetting to filter temperatures_ind for rows where the city is in cities.
"""

# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])