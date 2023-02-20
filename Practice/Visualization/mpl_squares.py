import matplotlib.pyplot as plt

#Входные данные
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#Стиль
plt.style.use('fivethirtyeight')

#Переменные для построения графика функцией: fig - сам график, ax - линия графика
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

#Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Squaes of values", fontsize=14)

#Деления на осях и размер шрифта
ax.tick_params(axis='both', labelsize=14)

plt.show()