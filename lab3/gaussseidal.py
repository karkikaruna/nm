import numpy as np
import pandas as pd

n = int(input("Enter the number of variables : "))
A = []

print("Enter the augmented matrix (each row with coefficients and constant term):")
for i in range(n):
    A.append(list(map(float, input(f"Row {i+1}: ").split())))

A = np.array(A)
print(f"\nThe augmented matrix A:\n{A}")

coeff_matrix = A[:, :-1]
const_terms = A[:, -1]

X = []
print("\nEnter the initial guess values:")
for i in range(n):
    X.append(float(input(f"x{i+1} initial guess: ")))

X = np.array(X)
print(f"\nInitial guesses:\n{X}")

e = float(input("\nEnter the tolerable error: "))
N = int(input("Enter the maximum number of iterations: "))

iteration = 0
itr_table = []

while iteration < N:
    X_old = X.copy()

    for i in range(n):
        s = sum(coeff_matrix[i][j] * X[j] for j in range(n) if j != i)
        X[i] = (const_terms[i] - s) / coeff_matrix[i][i]

    itr_table.append([iteration + 1] + list(X))

    if np.all(np.abs(X - X_old) < e):
        break

    iteration += 1

if iteration == N:
    print(f"\nSolution not found within {N} iterations.")
else:
    print(f"\nSolution found in {iteration+1} iterarion:")
    print("\nThe solution is :")
    for i in range(n):
        print(f"x{i+1} = {X[i]:.4f}")
