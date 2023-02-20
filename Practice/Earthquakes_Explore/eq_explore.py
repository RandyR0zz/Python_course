import json

#Изучение структуры данных, открытие файла
filename = "D:\IT_Learning_Folder\Practice\Projects\Earthquakes_Explore\eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

#Изучение структуры данных, загрузка данных (indent - форматирование данных с отступами, соответсвующими структуре)
readable_file = "D:\IT_Learning_Folder\Practice\Projects\Earthquakes_Explore\_readable_eq_data.json"
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

#Извлечение данных магнитуд, долгот, широт
all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lats)

print(mags[:10])
print(lons[:5])
print(lats[:5])

