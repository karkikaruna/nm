# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# eqn=input('Enter the equation in x using python syntax: ')
# def F(x,eqn):
#     return eval(eqn)
# def f(x):
#     return F(x, eqn)

# a,b=float(input('Enter the first initial guess: ')), float(input('Enter the second initial guess: '))
# if f(a)*f(b)>0:
#     print(f'No root lies in the interval ({a},{b})')

# else:
#     e,N=float(input("Enter the tolerable error: ")), int(input("Enter the Maximum iterations: "))
#     itr=1
#     A=[]
#     m=[]
#     while itr<=N:
#         fa=f(a)
#         fb=f(b)
#         c=(a*fb-b*fa)/(fb-fa)
#         fc=f(c)
#         A.append([itr, a, b, c, fa, fb, fc])
#         m.append(c)
#         err=abs(fc)
#         if err<e:
#             break
#         if fa*fc<0:
#             b=c
#         else:
#             a=c
#         if abs(b-a)<e:
#             break
#         itr+=1
#     df=pd.DataFrame(A, columns=['Iteration', 'a', 'b', 'c', 'f(a)', 'f(b)', 'f(c)'])
#     print(df)
#     if itr<=N:
#         print(f'The approximate root is {c} found in {itr} iterations')

#     else:
#         print(f'Solution did not converge in {N} iterations')
#     m=np.array(m)
#     x=np.linspace(-5, 5, 1000)
#     plt.plot(x, f(x), label=f'f(x)={eqn}')
#     plt.axhline(0,0,color='black') 
#     plt.axvline(0,0, color='black')
#     plt.grid(True)
#     plt.title('Regula falsi method: function plot')
#     plt.xlabel('x')
#     plt.ylabel('f(x)')
#     plt.legend()
#     plt.scatter(m,f(m), color='green')
#     for i,val in enumerate (m):
#         plt.text(val, f(val),f'{i+1}')
#     plt.show()     
import numpy as np
import pandas as pd
eqn=input("Enter equation in x using python syntax.")
def F(x,eqn):
    return eval(eqn)
def f(x):
    return F(x,eqn)
a,b=float(input("Enter first initial guess: ")), float(input("ENter second initial guess: "))
if f(a) *f(b)>0:
    print(f"Root does not lies between {a}, {b}")
else:
    e,N=float(input("Enter tolerable error: ")), int(input("Enter maximum number of iterarion: "))
    itr=1
    while(itr<N):  
        c=a-f(a)*((b-a)/(f(b)-f(a)) ) 
        if f(c)*f(b)<0:
            b=c
        else:
            a=c      

       