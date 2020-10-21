# RENAMING COLUMNS
import pandas as pd

# METHOD 1, YOU GOTTA CHANGE ALL THE COLUMNS NAMES

df = pd.read_csv('imdb.csv')

# Rename columns here
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)

# METHOD 2 THROUGH DICTIONARY, MUCH BETTER CAUSE YOU CAN EDIT EVEN JUST ONE COLUMN AND U DON'T CALL ERRORS

df1 = pd.read_csv('imdb.csv')

# Rename columns here
df1.rename(columns={'name': 'movie_title'},
          inplace=True)
print(df1)
