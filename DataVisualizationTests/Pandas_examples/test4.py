# RENAMING COLUMNS
import pandas as pd

# METHOD 1, YOU GOTTA CHANGE ALL THE COLUMNS NAMES

df0 = pd.read_csv('imdb.csv')

# Rename columns here
df0.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df0)

# METHOD 2 THROUGH DICTIONARY, MUCH BETTER CAUSE YOU CAN EDIT EVEN JUST ONE COLUMN AND U DON'T CALL ERRORS

df1 = pd.read_csv('imdb.csv')

# Rename columns here
df1.rename(columns={'name': 'movie_title'},
           inplace=True)
print(df1)


# USING LAMBDA FUNCTION TO SELECT ROWS AND
# TO CALCULATE THE TOTAL INCOME OF THE EMPLOYEES

df2 = pd.read_csv('employees.csv')

# Add columns here
get_last_name = lambda name: name.split()[-1]
df2['last_name'] = df2.name.apply(get_last_name)

total_earned = lambda row: row['hours_worked'] * row['hourly_wage'] if row['hours_worked'] <= 40 else \
    (row['hourly_wage'] * 40) + (row['hours_worked'] - 40) * (row['hourly_wage'] * 1.50)

total_earned1 = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
    if row.hours_worked > 40 \
    else row.hourly_wage * row.hours_worked

# df['total_wage'] = df.apply()

df2['total earned'] = df2.apply(total_earned1, axis=1)

print(df2)


# creating greetings column
orders = pd.read_csv('shoefly.csv')

print(orders.head())

orders['shoe_source'] = orders.shoe_material.apply(lambda material: 'vegan' if material != 'leather' else 'animal')

salutation = lambda row: 'Dear Mr. {}'.format(row.last_name) if row.gender == 'male' else 'Dear Ms. {}'.format(row.last_name)

orders['salutation'] = orders.apply(salutation, axis=1)

print(orders)