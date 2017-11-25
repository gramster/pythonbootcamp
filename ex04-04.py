# Select just the 'animal' and 'age' columns from the DataFrame.
df[['animal', 'age']]

# Select the data in rows [3, 5, 7] and in columns ['animal', 'age'].
df.loc[3:7:2, ['animal', 'age']]


