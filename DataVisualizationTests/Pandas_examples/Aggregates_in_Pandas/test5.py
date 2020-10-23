import pandas as pd
import numpy as np

""" Command	Description
    mean:	Average of all values in column
    std:	Standard deviation
    median:	Median
    max:	Maximum value in column
    min:	Minimum value in column
    count:	Number of values in column
    nunique:	Number of unique values in column
    unique:	List of unique values in column
    """

""""In general, we use the following syntax to calculate aggregates:
df.groupby('column1').column2.measurement()

where:
column1 is the column that we want to group by ('student' in our example)
column2 is the column that we want to perform a measurement on (grade in our example)
measurement is the measurement function we want to apply (mean in our example)"""

orders = pd.read_csv('orders.csv')

print(orders.head(10))

most_expensive = orders.price.max()  # CALCULATING COLUMN STATISTIC

num_colors = orders.shoe_color.nunique()  # CALCULATING COLUMN STATISTIC

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()  # CALCULATING AGGREGATE FUNCTIONS 1
# teas_counts = teas.groupby('category').id.count().reset_index() # 2 YOU CAN RENAME THE COLUMNS

# # CALCULATING AGGREGATE FUNCTIONS 3
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()

# CALCULATING AGGREGATE FUNCTIONS 4
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()  # PIVOT TABLES

shoe_counts_pivot = shoe_counts.pivot(
    columns='shoe_color',
    index='shoe_type',
    values='id'
).reset_index()

print(pricey_shoes)
print(num_colors)
print(cheap_shoes)
print(shoe_counts)
print(shoe_counts_pivot)
