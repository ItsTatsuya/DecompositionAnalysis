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
    n = len(matrix)
    lower = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            sum_ = np.sum(lower[i, :j] * lower[j, :j])
            if i == j:
                lower[i, j] = np.sqrt(matrix[i, i] - sum_)
            else:
                lower[i, j] = (1.0 / lower[j, j]) * (matrix[i, j] - sum_)

    end_time = time.time_ns()
    print('CL decomposition time: ', end_time - start_time, 'ns',"\n")
    return end_time - start_time


# LU Decomposition
def LU_decomposition(matrix):
    start_time = time.time_ns()
    m, n = matrix.shape
    l = np.zeros((m, n))
    u = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            u[i, j] = matrix[i, j] - np.dot(l[i, :i], u[:i, j])

        for j in range(i + 1, m):
            l[j, i] = (matrix[j, i] - np.dot(l[j, :i], u[:i, i])) / u[i, i]

    end_time = time.time_ns()
    print('LU decomposition time: ', end_time - start_time, 'ns',"\n")
    return end_time - start_time


# QR Decomposition
def QR_decomposition(matrix):
    start_time = time.time_ns()
    m, n = matrix.shape
    q = np.zeros((m, n))
    r = np.zeros((n, n))

    for i in range(n):
        v = matrix[:, i].copy()

        for j in range(i):
            r[i, j] = np.dot(q[:, j], matrix[:, i])
            v = v - r[i, j] * q[:, j]

        r[i, i] = np.linalg.norm(v)
        q[:, i] = v / r[i, i]
        
    end_time = time.time_ns()
    print('QR decomposition time: ', end_time - start_time, 'ns',"\n")
    return end_time - start_time