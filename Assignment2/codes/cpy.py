import numpy as np
from ctypes import *
cpy=CDLL('./cpy.so')
div=cpy.div
sub=cpy.sub
mod=cpy.mod
div.restype=c_float
sub.restype=c_float
mod.restype=c_float

data = np.loadtxt('dat.txt', delimiter=';', dtype=str)

if data.shape[0] < 2:
    raise ValueError("Not enough data points in 'dat.txt'.")

x = data[:, 0].astype(float)
y = data[:, 1].astype(float)
labels = data[:, 2]

data = np.loadtxt('dat.txt', delimiter=';', dtype=str)

q=mod(c_float(x[0]),c_float(y[0]))
r=mod(c_float(x[2]),c_float(y[2]))
d=sub(c_float(q),c_float(r))
k=div(c_float(d))
print("k=",k)
print("Q=(3,",k,")")
print("R=(",k,",5)")
