import pandas as pd
import numpy as np
n= int(input("ENter the order of square matrix: "))
A=[]
B=[]
tbl=[]
for i in range(n):
    A.append(list(map(float, input(f"ENter row {i+1}: ").split())))

A=np.array(A)
print("The matrix is A: \n" ,np.matrix(A))
x=np.array(list(map(float,input("ENter the initial vector: ").split())))
x=np.array(x)
e,N=float(input("ENter the tolerable error: ")), int(input("ENter the number of iterations: "))
itr=1
oldev=0
def inv(A):
    try:
        return np.linalg.inv(A)
    except:
        print('Matrix is singular')
B=np.matrix(inv(A))        
while itr<=N:
    
    Y=np.dot(B,x)
    maxev=abs(max(Y, key=abs))
    tbl.append([itr, oldev, maxev]) 
    for i in range (n):
        x=Y/maxev
    err=abs(oldev-maxev)
    if err<e:
        break
    oldev=maxev
    itr+=1
if itr>N:
    print(f'NO dominant eigenvalue found in {N} iterations.')
else:
    # tbl=pd.DataFrame(tbl, columns=['iteration', 'oldev', 'maxev'])
    print(f'THe dominatnt eigenvalue is {maxev} in {itr} iteration.\n')
    print("THe corresponding eigenvalue is x:\n", np.matrix(x)) 
     


    