import matplotlib.pyplot as plt
import sympy as sy
import numpy as np
import math


# Fixed point iteration method with function g given first point x0 and a tolarance 
def fixedPointIter(g,x0,TOL):
    PP = []
    Err = float("inf") # |Xn - alpha| ~ |g'(a)|*|Xn - Xn+1| -> It should be this but I couldn't diff the G(x)
    
    while Err >= TOL:
        p = g(x0)
        Err = abs(p-x0)
        x0 = p
        PP.append(p)
    return p, PP

# Atkins iteration
def atkinIter(g,x0,TOL):
    PP = [] # list of points(roots)
    Err = float("inf")
    a_iter = lambda p0, p1, p2: p0 - (math.pow((p1-p0),2)/((p2-p1) - (p1-p0)))# -> p3 
    # We iterate twice for initial values
    p0 = x0
    p1 = g(p0)
    p2 = g(p1)

    distSolution = g(p2)-p2 # dist to solution
    atkinP2 = a_iter(p0,p1,p2) # atkin approximation for p2
    distAtkinSolution = g(atkinP2)- atkinP2 # atkin dist to solution

    while Err >= TOL:
        if abs(distAtkinSolution) > abs(distSolution):
            p0 = p2
            p1 = g(p0)
            p2 = g(p1)

            PP.append(p0)
            PP.append(p1)
            PP.append(p2)

            # We check again if we should continue with g(x) or with Atkin Method
            distSolution = g(p2)-p2 # dist to solutiont
            atkinP2 = a_iter(p0,p1,p2) 
            distAtkinSolution = g(atkinP2)- atkinP2 
        else:
            p0 = a_iter(p0,p1,p2)
            distAtkinSolution = g(p0) - p0
            PP.append(p0)

        Err = abs(p0-g(p0))

    return p0, PP

# Stephensen iteration
def stephensenIter(g,x0,TOL):
    PP = [] # list of points(roots)
    Err = float("inf")
    a_iter = lambda p0, p1, p2: p0 - (math.pow((p1-p0),2)/((p2-p1) - (p1-p0)))# -> p3 
    # We perform a few iterations
    p0 = x0
    p1 = g(p0)
    p2 = g(p1)

    while Err >= TOL:
        p0 = a_iter(p0,p1,p2)
        p1 = g(p0)
        p2 = g(p1)
        Err = abs(p2-p1)

        PP.append(p0)

    return p2, PP


# def f(x):
#     return math.pow(x,3) - 2*math.pow(x,2) + x

# def fDiff(x): # We could use sympy but f'(x) can be solved easily
#     return 3*math.pow(x,2) - 4*x + 1

# def g(x):
#     return x - 2*(f(x))/(fDiff(x))

def g(x):
    return 2/x-1

def conv(xn,xnp1,xnm1,xnm2):
    print(abs(xnp1 - xn)/abs(xn - xnm1))
    up = math.log(abs(abs(xnp1 - xn)/abs(xn - xnm1)))
    down = math.log(abs(abs(xn-xnm1)/abs(xnm1-xnm2)))
    return up/down

p, PP = stephensenIter(g,-1.7,10e-6)

for i in PP:
    print(i)

# print(conv(PP[2],PP[3],PP[1],PP[0]))

