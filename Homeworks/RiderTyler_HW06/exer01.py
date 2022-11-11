''' Homework 06 - Exercise 01 '''

import matplotlib.pyplot as plt

fruitNames = ["Apples", "Oranges", "Cherries", "Watermelon"]
fruitQuantity_2020 = [25, 25, 10, 18]
fruitQuantity_2021 = [22, 18, 9, 19]

fig, sp = plt.subplots(2, 2, figsize=(12, 10))
chart, scatter, stack, pie = sp.flatten()
fig.canvas.manager.set_window_title("Exercise 01 Subplots")

# First Plot
chart.title.set_text("Plot Plot")
chart.set_xlabel("Fruit Name")
chart.set_ylabel("Fruit Quantity")
chart.plot(fruitNames, fruitQuantity_2020, label='2020', color='b')
chart.plot(fruitNames, fruitQuantity_2021, label='2021', color='c')
chart.legend()

# Second Plot
scatter.title.set_text("Scatter Plot")
scatter.set_xlabel("Fruit Name")
scatter.set_ylabel("Fruit Quantity")
scatter.scatter(fruitNames, fruitQuantity_2020, label='2020', color='b')
scatter.scatter(fruitNames, fruitQuantity_2021, label='2021', color='c')
scatter.legend()

# Third Plot
stack.title.set_text("Stack Plot")
stack.set_xlabel("Fruit Name")
stack.set_ylabel("Fruit Quantity")
stack.stackplot(fruitNames, fruitQuantity_2020, fruitQuantity_2021, labels=["2020", "2021"], colors=['b', 'c'])
stack.legend(loc="upper right")

# Fourth Plot 
# summedQuantities = [x + y for x, y in zip(fruitQuantity_2020, fruitQuantity_2021)]
pie.title.set_text("Pie Plot")
pie.pie([x + y for x, y in zip(fruitQuantity_2020, fruitQuantity_2021)], labels=fruitNames)

# Show Plot
plt.suptitle("Plots of Fruit Information", fontsize=20)
plt.show()