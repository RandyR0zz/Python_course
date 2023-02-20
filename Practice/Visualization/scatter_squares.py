import matplotlib.pyplot as plt

#Нанесение отдельных точек, атрибут s в функции scatter отвечает за жирность точки, c - за цвет
x_values = list(range(1, 10))
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='green', s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squaes of values", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

#Диапозон для каждой оси
ax.axis([0, 10, 0, 100])

plt.show()

#plt.savefig('squares_plot.png', bbox_index='tight') - сохранение (второй аргумент можно опустить)