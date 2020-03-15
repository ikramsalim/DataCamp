# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[(homelessness["individuals"] > 10000)]

# See the result
print(ind_gt_10k)

"""
There are many ways to subset a DataFrame, perhaps the most common is 
to use relational operators to return True or False for each row,
 then pass that inside square bracket
 
dogs[dogs["height_cm"] > 60]
dogs[dogs["color"] == "tan"]
"""
# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)


"""
You can filter for multiple conditions at once by using the "logical and" operator, &

dogs[(dogs["height_cm"] > 60) & (dogs["col_b"] == "tan")]
"""

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000 ) & ( homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)