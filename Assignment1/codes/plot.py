import matplotlib.pyplot as plt

x = [1, -4, -3/2]
y = [-5, 5, 0]
labels = ['A(1,-5)', 'B(-4,5)', 'C(-3/2,0)']

plt.figure()

plt.scatter(x, y, color='red')
plt.plot(x, y, color='blue', linestyle='--', marker='o')

plt.annotate(labels[0], (x[0], y[0]), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(labels[1], (x[1], y[1]), textcoords="offset points", xytext=(0,10), ha='center')
plt.annotate(labels[2], (x[2], y[2]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.title('Graph')

plt.savefig('plot.png')

plt.show()

