import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,6])
y = np.array([11,88])

# plt.subplot(1, 2, 1) #the figure has 1 row, 2 columns, and this plot is the first plot.
# plt.title("data visulization")
# plt.plot(x,y)
# plt.show()

points = np.array([65,1,66,89,9])

plt.subplot(1, 5, 1)
plt.title("LINE CHART")
plt.plot(points)

bar_chart_x = np.array(["X", "Y", "Z", "W"])
bar_chart_y = np.array([20,30,36,42]) 

plt.subplot(1, 5, 2)
plt.title("BAR CHART")
plt.bar(bar_chart_x,bar_chart_y)

# Scatter plot

scatter_x = np.array([7,5,11,29,21.45])
scatter_y = np.array([45,67,9.3, 76,31])

plt.subplot(1, 5, 3)
plt.title("Scatter CHART")
plt.scatter(scatter_x, scatter_y)

pie_value = np.array([20,34,64,10,50])

plt.subplot(1, 5, 4)
plt.title("PIE CHART")
plt.pie(pie_value)

histogram_value = np.random.normal(170,10,250)

plt.subplot(1, 5, 5)
plt.title("HISTOGRAM CHART")
plt.pie(histogram_value)

plt.show()
