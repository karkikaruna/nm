import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
eqn=input("Enter equation in x using python syntax: ")
def F(x, eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)
a,b=float(input("Enter first initial guess: ")), float(input("ENter second initial guess: "))

if f(a)*f(b)>0:
    print(f"Roots does not lies in the interval {a}, {b}")
else:
    e,N=float(input("ENter tolerable error: ")), int (input("ENter number of iterations: "))
    itr=1
    A=[]
    m=[]
    while itr<=N:
        c=(a+b)/2
        A.append([itr,a, b, c , f(a), f(b), f(c)])
        m.append(c)
        if f(a)*f(c)<0:
            b=c
        else:
            a=c    
        err=abs(b-a)
        if err<e:
            A=pd.DataFrame(A,columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
            print(A.to_string(index=False))
            print(f"The approximate root is: {c} in {itr } iterations. ")
            break
        itr+=1
    if (itr>N):
        print(f'solution does not converge in {N} iterations. ')    
        
m=np.array(m)
x=np.linspace(-5, 5, 1000)
plt.plot(x, f(x),color='green' ,label=eqn)
x=plt.axhline(0,0, color='black')
plt.axvline(0,0, color='yellow')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.title('Bisection Method.')
plt.scatter(m,f(m))
for i , val in enumerate(m):
    plt.text(val, f(val), f'{i+1}')
plt.show()    
    