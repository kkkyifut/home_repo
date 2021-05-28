import matplotlib.pyplot as plt
from random_walk import RandomWalk

# новые блуждания строятся до тех пор, пока программа активна
while True:
    # построение случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    # нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 5), dpi=137)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors='none', s=1)
    # ax.plot(rw.x_values, rw.y_values, linewidth=1)
    
    # выделение первой и последней точек
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
            s=100)
    
    # удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break