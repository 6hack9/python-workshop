import matplotlib.pyplot as plt
"""  a time-based dataset use a line plot. Some examples of a line plot include the plotting of heart rate, the visualization of population growth against time, or even the stock market. By creating a line plot, you are able to understand the trend and seasonality of data. """
stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42, 200.32, 200.32, 200.85, 199.2, 199.2, 199.2,
               199.46, 201.46, 197.54, 201.12, 203.12, 203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]

t = list(range(1, 31))
""" Plot this together with the data. You can also define the numbers on the x axis using xticks: """
plt.title('Opening Stock Prices')
plt.xlabel('Xaxis Days')
plt.ylabel('Yaxis Dollars $')
plt.plot(t, stock_price, marker='o', color='red')
plt.xticks([1, 8, 15, 22, 28])
plt.show()
