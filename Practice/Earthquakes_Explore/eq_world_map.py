import json

from plotly.graph_objs import Layout
from plotly import offline

#Изучение структуры данных, открытие файла
filename = "D:\IT_Learning_Folder\Practice\Projects\Earthquakes_Explore\eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

#Извлечение данных магнитуд, долгот, широт
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    text = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(text)

#Нанесение данных на карту
# data = [Scattergeo(lon=lons, lat=lats)] - простое нанесение

#Благодаря ключу marker в Plotly можно регулировать размер, цвет, диапозон и многе другое
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]

#Другие цветовые шкалы
# from plotly import colors

# for key in colors.PLOTLY_SCALES.keys():
#     print(key)

#Построение диаграммы 
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='D:\IT_Learning_Folder\Practice\Projects\Earthquakes_Explore\global_earthquakes.html')