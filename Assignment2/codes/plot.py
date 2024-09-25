import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('dat.txt', delimiter=';', dtype=str)

if data.shape[0] < 2:
    raise ValueError("Not enough data points in 'dat.txt'.")

x_coords = data[:, 0].astype(float)
y_coords = data[:, 1].astype(float)
labels = data[:, 2]

center_x = float(data[1, 0])
center_y = float(data[1, 1])
point_on_circle_x = float(data[0, 0])
point_on_circle_y = float(data[0, 1])

radius = np.sqrt((point_on_circle_x - center_x)**2 + (point_on_circle_y - center_y)**2)

plt.figure(figsize=(8, 8))

plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
_ = [plt.text(x, y, label, fontsize=8, ha='right') for x, y, label in zip(x_coords, y_coords, labels)]

circle = plt.Circle((center_x, center_y), radius, color='r', fill=False, linestyle='--')
plt.gca().add_artist(circle)

plt.xlim(-4, 4)
plt.ylim(-2, 6)

plt.axis('equal')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')
plt.grid(True)
plt.tight_layout()

plt.show()
plt.savefig("plot.png")

