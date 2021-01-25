import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
""" A scatter plot is suitable for visualizing a categorical dataset with numeric values """
temperature = [14.2, 16.4, 11.9, 12.5, 18.9,
               22.1, 19.4, 23.1, 25.4, 18.1, 22.6, 17.2]
sales = [215.20, 325.00, 185.20, 330.20, 418.60, 520.25,
         412.20, 614.60, 544.80, 421.40, 445.50, 408.10]
plt.scatter(temperature, sales, color='red')
plt.title('Ice-cream sales VS Temperature')
plt.ylabel('Temperatur')
plt.xlabel('Sales')
plt.show()
