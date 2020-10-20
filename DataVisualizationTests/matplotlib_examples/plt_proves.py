from matplotlib import pyplot as plt

# time = [0, 1, 2, 3, 4]
# revenue = [200, 400, 650, 800, 850]
# costs = [150, 500, 550, 550, 560]
#
# plt.plot(time, revenue, color='green', linestyle='--', marker='s')
# plt.plot(time, costs, linestyle=':', color='red', marker='*')
#
# # plt.show()
#
# months = range(12)
# temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
# flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
#
# plt.subplot(1, 2, 1)
# plt.plot(months, temperature)
# plt.subplot(1, 2, 2)
# plt.plot(flights_to_hawaii, temperature, 'o')
# # plt.show()
#
# x = range(7)
# straight_line = [0, 1, 2, 3, 4, 5, 6]
# parabola = [0, 1, 4, 9, 16, 25, 36]
# cubic = [0, 1, 8, 27, 64, 125, 216]
#
# plt.subplot(2, 1, 1)
#
# plt.plot(x, straight_line)
#
# plt.subplot(2, 2, 3)
# plt.plot(x, parabola)
#
# plt.subplot(2, 2, 4)
# plt.plot(x, cubic)
#
# plt.subplots_adjust(wspace=0.35, bottom=0.2)

# plt.show()

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here
legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']
plt.legend(legend_labels, loc=8)
# plt.show()

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')

plt.figure(figsize=(7, 3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')
plt.show()