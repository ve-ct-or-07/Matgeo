import numpy as np
import matplotlib.pyplot as plt

f1 = lambda x: x**2
f2 = lambda x: x + 6

a, b, c = 1, -1, -6
discriminant = b**2 - 4*a*c
root1 = (-b + np.sqrt(discriminant)) / (2*a)
root2 = (-b - np.sqrt(discriminant)) / (2*a)

x1, x2 = min(root1, root2), max(root1, root2)

x = np.linspace(x1 - 2, x2 + 2, 400)
plt.plot(x, f1(x), label='y = x^2', color='blue')
plt.plot(x, f2(x), label='y = x+6', color='orange')
plt.fill_between(x, f1(x), f2(x), where=(f2(x) > f1(x))&(x>0), color='lightgray', label='Area in Q1')
plt.fill_between(x, f1(x), f2(x), where=(f2(x) > f1(x))&(x<0), color='#87CEEB', label='Area in Q2')
plt.title('Area between curves y = x^2 and y = x+6 and x=0')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(x=0, color='red', linestyle='--', label='x = 0')
plt.scatter(-2, 4, color='blue')
plt.scatter(3, 9, color='blue')
plt.scatter(0, 6, color='blue')
plt.annotate(f'({-2}, {4})', (-2,4), textcoords="offset points",xytext=(0,10), ha='center')     
plt.annotate(f'({3}, {9})', (3,9), textcoords="offset points",xytext=(0,10), ha='center') 
plt.annotate(f'({0}, {6})', (0,6), textcoords="offset points",xytext=(0,10), ha='center') 
plt.legend()
plt.grid()
plt.show()
plt.savefig("plot.png")
