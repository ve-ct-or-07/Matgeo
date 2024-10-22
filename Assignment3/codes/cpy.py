import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from ctypes import *
cpy=CDLL('./cpy.so')

discriminant=cpy.discriminant
discriminant.argtypes = [c_double, c_double, c_double]
discriminant.restype = c_double

rootp=cpy.rootp
rootp.argtypes = [c_double, c_double, c_double]
rootp.restype = c_double

rootn=cpy.rootn
rootn.argtypes = [c_double, c_double, c_double]
rootn.restype = c_double

f1 = lambda x: x**2
f2 = lambda x: x + 6

data = np.loadtxt('dat.txt', delimiter=';', dtype=str)

if data.shape[0] < 2:
    raise ValueError("Not enough data points in 'dat.txt'.")
    
a, b, c =data[:].astype(float)

d = discriminant(c_double(a),c_double(b),c_double(c))
root1 = rootp(c_double(a),c_double(b),c_double(d))
root2 = rootn(c_double(a),c_double(b),c_double(d))

x1, x2 = min(root1, root2), max(root1, root2)

area, _ = spi.quad(lambda x: f2(x) - f1(x), x1, x2)

print(f"{area:.2f}")

