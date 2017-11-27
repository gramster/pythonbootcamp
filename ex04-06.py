# Calculate the mean age for each different type of animal.
df.groupby('animal').age.mean()

# Count the number of each type of animal.
df.animal.value_counts()

# Sort the data first by the values in the 'age' column in decending order,
# then by the value in the 'visits' column in ascending order.
df.sort_values(by=['age', 'visits'], ascending=[False, True])

# In the 'animal' column, change the 'snake' entries to 'python'.
df.loc[df.animal == 'snake', 'animal'] = 'python'

# The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 
#'yes' should be True and 'no' should be False.
df['priority'] = df.apply(lambda row: True if row.priority == 'yes' else False, axis=1)



