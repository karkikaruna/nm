import pandas as pd
import numpy as np
n= int(input("ENter the order of square matrix: "))
A=[]
tbl=[]
for i in range(n):
    A.append(list(map(float, input(f"ENter row {i+1}: ").split())))

A=np.array(A)
print("Matrix A: \n")
print(A) 
      
x=np.array(list(map(float,input("ENter the initial vector: ").split())))
print("Initial vector:\n")
# print(x)
x=np.array(x)
e,N=float(input("ENter the tolerable error: ")), int(input("ENter the number of iterations: "))
itr=1
oldev=0
itr_table=[]
while itr<=N:
    
    Y=np.dot(A,x)
    maxev=abs(max(Y, key=abs))
    tbl.append([itr, oldev, maxev]) 
    for i in range (n):
        x=Y/maxev
    err=abs(oldev-maxev)
    itr_table.append(['itr', 'max_ev'] + [x[i] for i in range(n)])
    if err<e:
        itr_table=pd.DataFrame(itr_table, columns=['itr', 'Eigenvalue']+ [f'x{i+1}' for i in range (n)])
        print(itr_table)
        break
    oldev=maxev
    itr+=1
if itr>N:
    print(f'NO dominant eigenvalue found in {N} iterations.')
else:
    print(f'The dominant eigenvalue is: {maxev} in {itr} iterations.')
    print(f'The corresponding eigen vector is {x}')

