import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = "D:\IT_Learning_Folder\Practice\Projects\Sitka_highs\data\sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Чтение максимальных температур
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            highs.append(high)
            dates.append(current_date)
            lows.append(low)

#Нанесение данных на диаграмму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Форматирование диаграммы
title = "Daily high and low temperatures, 2018"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()