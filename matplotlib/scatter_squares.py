import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# назначение размера шрифта елений на осях
ax.tick_params(axis='both', which='major', labelsize=14)
# назначение диапазона для каждой оси
# ax.axis([0, 1100, 0, 1100000])

plt.show()
# метод для сохранения файла, 2 аргумент обрезает пустое пространство по краям
# plt.savefig('squares_plot.png', bbox_inches='tight')