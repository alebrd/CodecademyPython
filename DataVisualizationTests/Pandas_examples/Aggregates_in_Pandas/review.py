import pandas as pd

user_visits = pd.read_csv('page_visits.csv')

print('*' * 60)
print(user_visits.head())
print('*' * 60)
click_source = user_visits.groupby('utm_source').id.count().reset_index()

print(click_source)
print('*' * 60)

click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

print(click_source_by_month)
print('*' * 60)

click_source_by_month_pivot = click_source_by_month.pivot(
  columns='month',
  index='utm_source',
  values='id'
).reset_index()

print(click_source_by_month_pivot)
print('*' * 60)
