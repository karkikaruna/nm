import numpy as np
import scipy.linalg as slg

n=int(input("No.of variables: ")) 
A=[]

for i in range(n):
    A.append(list(map(float, input(f"ENter row {i+1}: ").split())))

print("The coefficient matrix is:A\n ",np.matrix(A))
B=np.array(list(map(float, input('Enter the column terms: ').split())))
B=np.array(B)
print("The output matrix is B: \n", np.matrix(B))
P,L,U=slg.lu(A)
lum=slg.lu_factor(A)
print(f"THe lower triangular matrix L:\n",np.matrix(L))
print(f"THe upper triangular matrix U\n", np.matrix(U))
print(f"The permutation matrix is P:\n", np.matrix(P))
x=slg.lu_solve(lum, B)
print(f'The solution vector X is :\n', np.matrix(x))




