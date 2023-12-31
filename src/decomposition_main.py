import numpy as np
import time
import matplotlib.pyplot as plt
import csv

def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            values = list(map(float, row))
            int_values = list(map(int, values))
            matrix.append(int_values)
    return np.array(matrix)

def cholesky_decomposition(matrix):
    start_time = time.time_ns()
    n = matrix.shape[0]
    lower = np.zeros_like(matrix, dtype=np.float64)

    for i in range(n):
        diag_element = np.sqrt(matrix[i, i] - np.sum(lower[i, :i] ** 2))
        lower[i, i] = diag_element
        lower[i+1:, i] = (1.0 / diag_element) * (matrix[i+1:, i] - np.dot(lower[i+1:, :i], lower[i, :i]))

    end_time = time.time_ns()
    #print('CL decomposition time:', end_time - start_time, 'ns',"\n")
    return end_time - start_time


# LU Decomposition
def LU_decomposition(matrix):
    start_time = time.time_ns()
    n = matrix.shape[0]
    l = np.zeros_like(matrix, dtype=np.float64)
    u = np.zeros_like(matrix, dtype=np.float64)

    for i in range(n):
        u[i, i:] = matrix[i, i:] - np.dot(l[i, :i], u[:i, i:])

        l[i+1:, i] = (matrix[i+1:, i] - np.dot(l[i+1:, :i], u[:i, i])) / u[i, i]

    end_time = time.time_ns()
    #print('LU decomposition time: ', end_time - start_time, 'ns',"\n")
    return end_time - start_time


# QR Decomposition
def QR_decomposition(matrix):
    start_time = time.time_ns()
    n = matrix.shape[0]
    q = np.zeros_like(matrix, dtype=np.float64)
    r = np.zeros_like(matrix, dtype=np.float64)

    for i in range(n):
        v = matrix[:, i].copy().astype(np.float64)  # Convert to float64

        for j in range(i):
            r[i, j] = np.dot(q[:, j], v)
            v -= r[i, j] * q[:, j]

        r[i, i] = np.linalg.norm(v)
        q[:, i] = v / r[i, i]
        
    end_time = time.time_ns()
    #print('QR decomposition time: ', end_time - start_time, 'ns',"\n")
    return end_time - start_time