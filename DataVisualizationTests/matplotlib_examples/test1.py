from matplotlib import pyplot as plt
x = [x for x in range(8)]
y1 = [1, 3, 4, 7, 4, 9, 6, 12]
y2 = [2, 3, 9, 8, 6, 8, 5, 15]

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o', linestyle='--')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(['Amazing X-axis', 'Incredible Y-axis'], loc=4)
# plt.show()
plt.subplot(1, 2, 2)
plt.plot(x, y1, color='red', marker='o', linestyle='--')
plt.plot(x, y2, color='purple', marker='o', linestyle='--')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(['Amazing X-axis', 'Incredible Y-axis'], loc=4)
plt.subplots_adjust(wspace=0.35, bottom=0.2)
plt.show()

'''
left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label

right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, 
or decrease it to make room for a legend

bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or 
an x-axis label

top — the top margin, with a default of 0.9

wspace — the horizontal space between adjacent subplots, with a default of 0.2

hspace — the vertical space between adjacent subplots, with a default of 0.2

'''