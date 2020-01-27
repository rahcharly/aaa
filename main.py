from sympy import pprint, init_printing, Symbol, sin, cos, exp, sqrt, series, Integral, Function
# Alternatively, you can call init_printing() once and pretty-print without the pprint function.
init_printing()
x = Symbol("x")
y = Symbol("y")
f = Function('f')
pprint(sqrt(sqrt(exp(x))))
pprint((1/cos(x)).series(x, 0, 10))

from sympy import init_printing, Symbol, expand
init_printing()
a = Symbol('a')
b = Symbol('b')
e = (a + b)**5
pprint(e)
pprint(e.expand())

from sympy import Rational, pprint
e = Rational(2)**50 / Rational(10)**50
pprint(e)
