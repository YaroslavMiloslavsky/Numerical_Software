import scipy.integrate as integrate
import numpy as np
import math

x = np.linspace(0,1,500)
valuesSet = list()

# Direct integration needed for checking our numerical metohds
def integrateDirect(a):
    for n in range(1,31):
        I = integrate.quad(lambda x: (math.pow(x,2*n))/(1+a*math.pow(x,2)) ,0,1)
        print(f'Iteration {n} = {I[0]}')
        valuesSet.append(I[0])
    return valuesSet

# An integral via recursive formula I_n
def integrateRecursion(a)->tuple:
    absoluteError = list()
    # First member of the series n=1
    I1 = integrate.quad(lambda x: (math.pow(x,2*1))/(1+a*math.pow(x,2)), 0 ,1)
    prevI = I1[0]
    absoluteError.append(abs(prevI - valuesSet[0]))
    print(f'Iteration {1} = {I1[0]}')

    for n in range(2,31):
        newI = 1/a * (1/(2*n-1) - prevI)
        absoluteError.append(abs(newI - valuesSet[n-1]))
        print(f'Iteration {n} = {newI}')
        prevI = newI

    return tuple(absoluteError)

# An integral via backward recursive formula I_n-1
def integrateBackwardRecursion(a)->tuple:
    absoluteError = list()
    # Last member of the series n=1
    I1 = integrate.quad(lambda x: (math.pow(x,2*30))/(1+a*math.pow(x,2)), 0 ,1)
    prevI = I1[0]
    absoluteError.append(abs(prevI - valuesSet[len(valuesSet)-1]))
    print(f'Iteration {30} = {I1[0]}')
    for n in range(29,0,-1):
        newI = 1/(2*n - 1) * (a - prevI)
        absoluteError.append(abs(newI - valuesSet[n-1]))
        print(f'Iteration {n} = {newI}')
        prevI = newI
    absoluteError.reverse()
    return tuple(absoluteError)

# print('--------- Direct Integration ---------')
print('0.1')
integrateDirect(0.1)
print('\n10')
integrateDirect(10)
# print('\n--------- Forward Recursive Formula Integration ---------')
# print('0.1')
# absErr1 = integrateRecursion(0.1)
# print('\n10')
# absErr2 = integrateRecursion(10)
print('\n--------- Backward Recursive Formula Integration ---------')
print('0.1')
absErr3 = integrateBackwardRecursion(0.1)
print('\n10')
absErr4 = integrateBackwardRecursion(10)


import matplotlib.pyplot as plt

plt.plot(absErr3)
plt.title('0.1 Error')
plt.xlabel('Index')
plt.ylabel('Error Value')
plt.show()

plt.plot(absErr4)
plt.title('10 Error')
plt.xlabel('Index')
plt.ylabel('Error Value')
plt.show()