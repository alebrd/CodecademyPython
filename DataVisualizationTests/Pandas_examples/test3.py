# ADDING COLUMNS METHODS

import pandas as pd

# METHOD 1
df = pd.DataFrame([
    [1, '3 inch screw', 0.5, 0.75],
    [2, '2 inch nail', 0.10, 0.25],
    [3, 'hammer', 3.00, 5.50],
    [4, 'screwdriver', 2.50, 3.00]
],
    columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

# METHOD 2
df1 = pd.DataFrame([
    [1, '3 inch screw', 0.5, 0.75],
    [2, '2 inch nail', 0.10, 0.25],
    [3, 'hammer', 3.00, 5.50],
    [4, 'screwdriver', 2.50, 3.00]
],
    columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df1['Is taxed?'] = 'Yes'
print(df1)

# METHOD 3

df2 = pd.DataFrame([
    [1, '3 inch screw', 0.5, 0.75],
    [2, '2 inch nail', 0.10, 0.25],
    [3, 'hammer', 3.00, 5.50],
    [4, 'screwdriver', 2.50, 3.00]
],
    columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here
df2['Revenue'] = df2.Price - df2['Cost to Manufacture']
print(df2)


# PERFORMING COLUMN'S OPERATIONS

def lowercase(my_string):
    return my_string.lower()


df3 = pd.DataFrame([
    ['JOHN SMITH', 'john.smith@gmail.com'],
    ['Jane Doe', 'jdoe@yahoo.com'],
    ['joe schmo', 'joeschmo@hotmail.com']
],
    columns=['Name', 'Email']
)

# Add column here
df3['Lowercase Name'] = df3.Name.apply(lowercase)
print(df)
