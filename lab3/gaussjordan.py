#to solve the system of linear equation using gauss jordan method
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
    A[i]=A[i]/A[i,i]
    for j in range (n):
        if j!=i:
            A[j]=A[j]-A[j,i]*A[i]
print('The upper triangular matrix is : ')
print(np.matrix(A))
x=A[:,-1]
print(x)

