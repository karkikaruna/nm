# #to solve the system of linear equation using gauss jordan method
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
#     A[i]=A[i]/A[i,i]
#     for j in range (n):
#         if j!=i:
#             A[j]=A[j]-A[j,i]*A[i]
# print('The upper triangular matrix is : ')
# print(np.matrix(A))
# x=A[:,-1]
# print(x)

import numpy as np

n = int(input("Enter the number of variables: "))
print("Enter augmented matrix :")
A = []

for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A)
print("The augmented matrix is:\n", A)

for i in range(n):
    P_row = np.argmax(abs(A[i:, i])) + i
    A[[i, P_row]] = A[[P_row, i]]

    A[i] = A[i] / A[i, i]


    for j in range(n):
        if j != i:
            A[j] = A[j] - A[j, i] * A[i]

print("\nThe matrix in Reduced form is:")
print(np.round(A, 4)) 

x = A[:, -1]
print("\nSolutions:")
for i in range(n):
    print(f"x{i+1} = {x[i]:.4f}")
