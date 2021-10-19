import math
import numpy as np
from scipy import integrate

np.seterr(divide='ignore')
def composite_trapezoidal_rule(function, h, x0, xn) -> float:
    main_sum = 0
    xi = x0 + h
    while xi < xn:
        main_sum = main_sum + function(xi)
        xi = xi + h

    return h / 2 * (function(x0) + 2 * main_sum + function(xn))


def composite_simspon_rule(function, h, x0, xn):
    main_sum = 0
    xi = x0 + h
    parity = False
    while xi < xn:
        if not parity:
            main_sum = main_sum + 4 * function(xi)
            xi = xi + h
            parity = True
        else:
            main_sum = main_sum + 2 * function(xi)
            xi = xi + h
            parity = False

    return h / 3 * (function(x0) + main_sum + function(xn))


def composite_midpoint_rule(function, h, x0, xn):
    main_sum = 0
    xi = x0 + h
    while xi < xn:
        main_sum = main_sum + function(xi)
        xi = xi + 2 * h
    return 2 * h * main_sum


# func1 = lambda x: math.pow(x, 2) * np.log(x)

# print(composite_trapezoidal_rule(func1, 0.25, 0, 2))
# print(composite_simspon_rule(func1, 0.25, 0, 2))
# print(composite_midpoint_rule(func1, 0.25, 0, 2))
def f(x) -> float:
    return x ** 3 + 2*(x**2)

while True:
    inp = float(input('enter x: '))
    print(f(inp))