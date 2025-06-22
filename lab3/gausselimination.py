#to solvve the system of linear equation by gauss elimination with partial pivoting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
n=int(input("Enter the number of variables: "))
print("Enter argumented matrix: ")
A=[]
for i in range(n):
    A.append(list(map(float, input(f"Enter {i+1}th row: ").split())))

A=np.array(A)
print("The argumented matrix is: \n", A)   
for i in range (n):
    P_row = np.argmax(abs(A[i:, i])) + i
    A[[i,P_row]] =A[[P_row, i]]
    for j in range (i+1, n):
        A[j]=A[j]-A[j,i]*A[i]/A[i,i]
print("The upper triangular matrix is: ",A)
print(np.matrix(A))   
x=np.zeros(n)
for i in range(n-1,-1,-1):
    x[i]=(A[i,-1]-np.sum(A[i, i+1:n]*x[i+1:n]))/A[i,i]
print("the solution is :")
for i in range(n):
    print(f'x{i+1}={x[i]}')


     
        


