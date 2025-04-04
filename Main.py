# Data Visualization
# Main.py

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_Species'])
print(iris.head())

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.head())

# create color dictionary
colors = {'Species': 'y', 'Iris-setosa': 'r', 'Iris-versicolor': 'g', 'Iris-virginica': 'b'}
print(iris['iris_Species'].unique())

# create a figure and axis
fig, ax = plt.subplots()

for i in range(len(iris['sepal_length'])):
    # scatter the sepal_length gaisnt speal_width
    #ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i])
    ax.scatter(iris['sepal_length'][i], iris['sepal_width'][i], color=colors[iris['iris_Species'][i]])

# set a title and label
ax.set_title('Iris Dataset')
ax.set_xlabel('sepal_length')
ax.set_ylabel('sepal_width')

columns = iris.columns.drop(['iris_Species'])

# create x data
x_data = range(0, iris.shape[0])

# create figure and axis
fig2, ax2 = plt.subplots()

# plot each column
for column in columns:
    ax2.plot(x_data, iris[column], label=column)

ax2.set_title('Iris Dataset')
ax2.legend()

# create figure and axis
fig3, ax3 = plt.subplots()

# plot histogram
ax3.hist(wine_reviews['points'])

# set title and labels
ax3.set_title('Wine Review Scores')
ax3.set_xlabel('Points')
ax3.set_ylabel('Frequency')

plt.show()