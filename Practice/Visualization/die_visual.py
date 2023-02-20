from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

#Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

#Анализ результатов
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#Визуализация результатов
x_values = list(range(1, die.num_sides+1))

#Набор Bar представляет из себя набор данных для построения столбцовых диаграмм
data = [Bar(x=x_values, y=frequencies)]

#Заголовки осей задаются в виде словарей
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

#Класс Layout возвращает объект, который создает диаграмму в целом
my_layout = Layout(title='Results of rolling one D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

#Функция для построения диаграммы
offline.plot({'data': data, "layout": my_layout}, filename='d6.html')