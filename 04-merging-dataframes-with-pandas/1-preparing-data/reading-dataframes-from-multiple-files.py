"""
Import pandas as pd.
Read the file 'Bronze.csv' into a DataFrame called bronze.
Read the file 'Silver.csv' into a DataFrame called silver.
Read the file 'Gold.csv' into a DataFrame called gold.
Print the first 5 rows of the DataFrame gold. This has been done for you, so hit 'Submit Answer' to see the results.
"""
# Import pandas
import pandas as pd

# Read 'Bronze.csv' into a DataFrame: bronze
bronze = pd.read_csv('Bronze.csv')

# Read 'Silver.csv' into a DataFrame: silver
silver = pd.read_csv('Silver.csv')

# Read 'Gold.csv' into a DataFrame: gold
gold = pd.read_csv('Gold.csv')

# Print the first five rows of gold
print(gold.head())

