from ctypes import *
cpy=CDLL('./cpy.so')
a1=1
b1=-5
a2=-4
b2=5
div=cpy.div
coord=cpy.coord
div.restype=c_float
coord.restype=c_float
k=-div(c_float(b1),c_float(b2))
x=coord(c_float(a1),c_float(a2),c_float(k))
y=coord(c_float(b1),c_float(b2),c_float(k)    )
print("Ratio=",k)
print("Point of division=(",x,",",y,")")
