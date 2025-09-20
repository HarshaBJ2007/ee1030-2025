import sympy as sp
import numpy as np
import ctypes

lib=ctypes.CDLL("./libmain.so")

lib.dir_vec.argtypes=(ctypes.c_double, ctypes.c_double, np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags="C_CONTIGUOUS"))

#given data
x=3
y=4

grad=np.empty(2, dtype=np.float64)

lib.dir_vec(x,y,grad)

norm_grad=np.linalg.norm(grad)
x=grad/norm_grad
unit_vec=sp.Matrix(x)
print("Unit vector along the direction of f:")
sp.pprint(unit_vec)

