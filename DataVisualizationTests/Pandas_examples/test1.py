import pandas as pd

from matplotlib import pyplot as plt

df = pd.read_csv('Bolt - Rider Invoices - October 2020 (1).csv')

df.head(10)

total = df['Price Total']
date = df.Date

# total1 = [i.reverse() for i in total]


plt.bar(date, total)
# plt.axis('equal')
ax = plt.subplot()
ax.set_xticks(range(6))
ax.set_xticklabels([x for x in range(6)])
plt.show()

print(df)
# print(total, date)