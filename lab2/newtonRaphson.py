import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in terms of x using Python syntax: ")

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

def g(f, x, h=1e-10):
    return (f(x + h) - f(x - h)) / (2 * h)

a = float(input("Enter the initial value: "))

if g(f, a) == 0:
    print("Choose another initial guess where derivative is not zero.")
else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the maximum number of iterations: "))
    itr = 1
    A = []
    B = []
    
    while itr <= N:
        fa = f(a)
        dfa = g(f, a)
        b = a - fa / dfa
        error = abs(b - a)
        fb = f(b)
        dfb = g(f, b)
        
        A.append([itr, a, b, fa, fb, dfa, dfb, error])
        B.append(b)
        
        if error < e:
            A = pd.DataFrame(A, columns=['iterations', 'a', 'b', 'f(a)', 'f(b)', 'g(a)', 'g(b)', 'error'])
            print(A.round(6))
            print(f'Approximate root is {b:.6f} in {itr} iterations\n')
            break
        
        a = b
        itr += 1

    if itr > N:
        print(f'Solution does not converge in {N} iterations')

x = np.linspace(-5, 5, 1000)
plt.plot(x, f(x), color='blue', label=eqn)
x=plt.axhline(0, 0,color='black')
plt.axvline(0,0, color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title("Newton Raphson method")       
for i, val in enumerate(B):
        plt.text(val, f(val), f'{i+1}')
plt.show()
