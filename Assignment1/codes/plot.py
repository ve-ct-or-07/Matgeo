import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('dat.txt', delimiter=';', dtype=str)

x_coords = data[:, 0].astype(float)
y_coords = data[:, 1].astype(float)
labels = data[:, 2]

plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')

_ = [plt.text(x, y, label, fontsize=12, ha='right') for x, y, label in zip(x_coords, y_coords, labels)]

plt.axis('equal')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.grid(True)
plt.savefig('plot.png')
plt.show()

