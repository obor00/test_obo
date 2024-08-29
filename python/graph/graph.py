import matplotlib.pyplot as plt

# Create sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 8]
y2 = [3, 4, 6, 8, 9]

# Create two subplots
plt.subplot(2, 1, 1)
plt.plot(x, y1, label='y1')
plt.legend(loc='upper left')

plt.subplot(2, 1, 2)
plt.plot(x, y2, label='y2')
plt.legend(loc='upper left')

# Save figure
plt.savefig('multiple_plots.png')
