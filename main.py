from src.matrix_gen import generate
from src.decomposition_main import LU_decomposition, QR_decomposition, cholesky_decomposition, read_matrix
from src.ratio_calc import ratio_calc, plot_graph

import csv
import numpy as np
import time 
import scipy.linalg as la
def main():
    # Generating the matrix
    matrix_size = int(input('Enter the size of the matrix: '))
    size = int(input('Enter the number of times you want to run the algorithms: '))
    file_name = 'asset/matrix.csv'
    generate(matrix_size, file_name)

    matrix = read_matrix(file_name)
    # Running the algorithms
    lu_times, qr_times, cl_times = [], [], []
    for i in range(size):
        lu_times.append(LU_decomposition(matrix))
        qr_times.append(QR_decomposition(matrix))
        cl_times.append(cholesky_decomposition(matrix))

        # Using the inbuilt functions
        '''start_time = time.time_ns()
        P,L,U = la.lu(matrix)
        end_time = time.time_ns()
        lu_times.append(end_time - start_time)

        start_time = time.time_ns()
        Q,R = la.qr(matrix)
        end_time = time.time_ns()
        qr_times.append(end_time - start_time)

        start_time = time.time_ns()
        C,L = la.cho_factor(matrix)
        end_time = time.time_ns()
        cl_times.append(end_time - start_time)'''


    # Storing the results in a csv file
    with open('asset/results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(lu_times)
        writer.writerow(qr_times)
        writer.writerow(cl_times)


    # Plotting the graph
    ratio_calc()

if __name__ == '__main__':
    main()