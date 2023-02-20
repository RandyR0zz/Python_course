import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Несколько случайных блужданий
while True:
    #Построение блуждания
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Нанесение точек
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    #Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break