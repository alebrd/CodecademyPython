from matplotlib import pyplot as plt

# STACKED BARS
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(drinks)), sales1)
plt.bar(range(len(drinks)), sales2, bottom=sales1)
plt.legend(['Location 1', 'Location 2'])

# plt.show()

# ERROR BARS
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)
# plt.show()

# FILL BETWEEN
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [i - 0.1 * i for i in revenue]
y_upper = [i + 0.1 * i for i in revenue]
# your work here
plt.plot(months, revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()

# PIE CHART
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct='%0.1f%%')
''''%0.2f' — 2 decimal places, like 4.08
     '%0.2f%%' — 2 decimal places, but with a percent sign at the end, like 4.08%. 
     You need two consecutive percent signs because the first one acts as an escape character, 
     so that the second one gets displayed on the chart.
     '%d%%' — rounded to the nearest int and with a percent sign at the end, like 4%.
'''
plt.axis('equal')
plt.legend(payment_method_names)

# plt.show()