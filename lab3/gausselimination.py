# #to solvve the system of linear equation by gauss elimination with partial pivoting
# import numpy as np
# n=int(input("Enter the number of variables: "))
# print("Enter argumented matrix: ")
# A=[]
# for i in range(n):
#     A.append(list(map(float, input(f"Enter {i+1}th row: ").split())))

# A=np.array(A)
# print("The argumented matrix is: \n", A)   
# for i in range (n):
#     P_row = np.argmax(abs(A[i:, i])) + i
#     A[[i,P_row]] =A[[P_row, i]]
#     for j in range (i+1, n):
#         A[j]=A[j]-A[j,i]*A[i]/A[i,i]
# print("The upper triangular matrix is: ",A)
# print(np.matrix(A))   
# x=np.zeros(n)
# for i in range(n-1,-1,-1):
#     x[i]=(A[i,-1]-np.sum(A[i, i+1:n]*x[i+1:n]))/A[i,i]
# print("the solution is :")
# for i in range(n):
#     print(f'x{i+1}={x[i]}')

import numpy as np

# Input number of variables
n = int(input("Enter the number of variables: "))

# Input augmented matrix
print("Enter the augmented matrix row-wise (each row should have n+1 values):")
A = []
for i in range(n):
    row = list(map(float, input(f"Enter row {i+1}: ").split()))
    if len(row) != n + 1:
        raise ValueError(f"Each row must have {n+1} elements.")
    A.append(row)

A = np.array(A)
print("\nInitial Augmented Matrix:")
print(A)

# Forward Elimination with Partial Pivoting
for i in range(n):
    # Partial Pivoting: find the row with max absolute value in current column
    pivot_row = np.argmax(abs(A[i:, i])) + i
    if A[pivot_row, i] == 0:
        raise ValueError("Matrix is singular or nearly singular.")
    
    # Swap rows
    A[[i, pivot_row]] = A[[pivot_row, i]]

    # Eliminate entries below the pivot
    for j in range(i+1, n):
        factor = A[j, i] / A[i, i]
        A[j] = A[j] - factor * A[i]

print("\nUpper Triangular Matrix:")
print(A)

# Back Substitution
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (A[i, -1] - np.dot(A[i, i+1:n], x[i+1:n])) / A[i, i]

# Output the solution
print("\nSolution:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")

        


