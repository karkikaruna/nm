import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n=int(input("Enter the number of variables: "))
print("Enter argumented matrix: ")
x=[]
A=[]
for i in range(n):
    x=np.array(list(map(float, input(f"Enter initial value : ").split())))

x=np.array(x)
print("The initial guess is: \n", np.matrix(x))
e,N= float(input("ENter tolerable error")), int (input("ENter maximum number of iterations: "))
itr=1
tbl=[]
while itr<=N:
    x_old=np.copy(x)
    for i in range(n):
        s=0
        for j in range (n):
            if j!=i:
                s+=A[i,i]*x[i]
                x[i]=(A[i,-1]-s)/A[i,i]
                tbl.append(x[itr]+x[i] for i in range (n))
                err=np.abs(x_old-x)
                if np.all(err<e):
                    break
                itr+=1
        if itr>N:
            print(f'solution does not converge in {N} iterations')
        else:
            print(f'solution converge in {N} iterations\n')
            print(x)

tbl.pd.Dataframe(tbl,columns=['Iteration'])

# import numpy as np

# n = int(input("Enter the number of variables: "))
# print("Enter augmented matrix coefficients row by row (including constants):")

# A = []
# for i in range(n):
#     row = list(map(float, input(f"Row {i + 1}: ").split()))
#     A.append(row)

# A = np.array(A)
# x = np.zeros(n)  
# e = float(input("Enter tolerable error: "))
# N = int(input("Enter maximum number of iterations: "))

# print("\nInitial guess:")
# print(x)

# print("\nIteration process:")
# for itr in range(1, N + 1):
#     x_old = x.copy()

#     for i in range(n):
#         s = 0
#         for j in range(n):
#             if j != i:
#                 s += A[i][j] * x[j] 
#         x[i] = (A[i][-1] - s) / A[i][i]

#     err = np.abs(x - x_old)
#     print(f"Iteration {itr}: {x}, Error: {err}")

#     if np.all(err < e):
#         print(f"\nSolution converged in {itr} iterations.")
#         break
# else:
#     print(f"\nSolution did not converge in {N} iterations.")

# print("\nFinal solution:")
# for i in range(n):
#     print(f"x{i+1} = {x[i]:.6f}")
         