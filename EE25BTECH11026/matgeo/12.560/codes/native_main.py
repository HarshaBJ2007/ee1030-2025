import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2

grad = sp.Matrix([sp.diff(f, v) for v in (x, y)])


norm_grad=grad.norm()
norm_val=norm_grad.subs({x:3,y:4})
grad_val = grad.subs({x:3, y:4})
unit_grad=grad_val/norm_val


print("Unit vector along the direction where f grows the fastest:")
sp.pprint(unit_grad)

