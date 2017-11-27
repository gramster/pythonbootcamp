# Select only the rows where the number of visits is greater than or equal to 3
df[df.visits>=3]

# Select the rows where the age is missing, i.e. is NaN
df[df.age.isnull()]

# Select the rows where the animal is a cat and the age is less than 3.
df[(df.age < 3) & (df.animal == 'cat')]

# Select the rows the age is between 2 and 4 (inclusive).
df[(df.age >= 2) & (df.age <= 4)]

# Change the index to use this list:
idx = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = idx

# Change the age in row 'f' to 1.5.
#df['age']['f'] = 1.5  # This will generate a warning; see http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
df.loc['f', 'age'] = 1.5

# Append a new row 'k' to df with your choice of values for each column. 
df.loc['k'] = (10, 'hippo', 0, 1)

# Then delete that row to return the original DataFrame.
df.drop(['k'], inplace=True)



