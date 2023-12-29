import numpy as np
import time
import matplotlib.pyplot as plt
import csv

def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            values = list(map(int, row))
            matrix.append(values)
    return matrix

# LU Decomposition
# LU Decomposition
def LU_decomposition(matrix):
    start_time = time.time_ns()
    n = len(matrix)
    L = np.eye(n)
    U = np.copy(matrix).astype(float)  # Explicitly cast U to float64

    for i in range(n):
        pivot = U[i, i]
        if pivot == 0:
            raise ValueError("LU decomposition failed: Zero pivot encountered.")
        
        L[i+1:, i] = U[i+1:, i] / pivot
        U[i+1:, i:] -= np.outer(L[i+1:, i], U[i, i:])
    
    end_time = time.time_ns()
    return end_time - start_time


# QR Decomposition
def QR_decomposition(matrix):
    start_time = time.time_ns()
    n = len(matrix)
    Q = np.eye(n)
    R = np.copy(matrix).astype(float)  # Explicitly cast R to float64

    for i in range(n):
        norm = np.linalg.norm(R[i:, i])
        if norm == 0:
            raise ValueError("QR decomposition failed: Zero norm encountered.")
        
        Q[i:, i:] = R[i:, i:] / norm
        R[i:, i:] -= 2 * np.outer(Q[i:, i], Q[i:, i:].T @ R[i:, i:])[:, :n-i]

    end_time = time.time_ns()
    return end_time - start_time

def cholesky_decomposition(matrix):
    start_time = time.time_ns()
    n = len(matrix)
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1):
            sum_L = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][i] = np.sqrt(max(matrix[i][i] - sum_L, 0))
            else:
                L[i][j] = (matrix[i][j] - sum_L) / L[j][j] if L[j][j] != 0 else 0
    end_time = time.time_ns()
    return end_time - start_time
