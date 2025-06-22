import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

eqn = input('Enter the equation in x using python syntax:\n')

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

a = float(input('Enter first initial approximation: '))
b = float(input('Enter second initial approximation: '))

if f(a) == f(b):
    print("Divide by zero error!")
else:
    e = float(input('Enter tolerable error: '))
    N = int(input('Enter maximum number of iterations: '))
    
    itr = 1
    A = []
    C = []

    while itr <= N:
        if f(b) - f(a) == 0:
            print("Divide by zero error!\n")
            break

        c = ((a * f(b) - b * f(a)) / (f(b) - f(a)))
        error = abs(c-b)
        A.append([itr, a, b, c, f(a), f(b), f(c), error])
        C.append(c)

        if error < e:
            df = pd.DataFrame(A, columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)', 'Error'])
            print(df.to_string(index=False))
            print(f'\nApproximate root is {c} in {itr} iterations')
            break

        a, b = b, c
        itr += 1

    if itr > N:
        print(f'Solution did not converge in {N} iterations.')

    x = np.linspace(-5, 5, 1000)
    y = [f(val) for val in x]
    plt.plot(x, y, label='f(x)', color='red')
    plt.axhline(0,0 ,color='blue')
    plt.axvline(0,0, color='green')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Secant Method')
    plt.legend()
    for i, val in enumerate(C):
        plt.text(val, f(val), f'{i+1}')
    plt.show()
