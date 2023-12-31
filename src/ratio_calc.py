#read the results.csv file and plot the graph, find the average time taken by each algorithm and plot the graph, and find the ratio of the average time taken by each algorithm and plot the graph.

import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def read_results(filename,row):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for i in range(row):
            next(csv_reader)
        row = next(csv_reader)
        times = list(map(int, row))
    return times

def plot_graph(x, y, title, x_label, y_label):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

def ratio_calc():
    lu_times = read_results('asset/results.csv',0)
    qr_times = read_results('asset/results.csv',1)
    cl_times = read_results('asset/results.csv',2)

    avg_lu_time = np.mean(lu_times)
    avg_qr_time = np.mean(qr_times)
    avg_cl_time = np.mean(cl_times)

    lu_ratio = avg_lu_time / avg_cl_time
    qr_ratio = avg_qr_time / avg_cl_time
    cl_ratio = 1  # avg_cl_time / avg_cl_time is always 1

    # Find the greatest common divisor (GCD) of all three ratios
    gcd = math.gcd(math.gcd(int(lu_ratio), int(qr_ratio)), int(cl_ratio))

    # Divide each ratio by the GCD
    lu_ratio /= gcd
    qr_ratio /= gcd
    cl_ratio /= gcd

    x = ['LU', 'QR', 'CL']
    y = [avg_cl_time, avg_qr_time, avg_cl_time]
    plot_graph(x, y, 'Comparison of Decomposition Algorithms', 'No of times run', 'time taken (nanoseconds)')

    print('Average time taken by LU decomposition: ', '{:,}'.format(avg_lu_time),'ns')
    print('Average time taken by QR decomposition: ', '{:,}'.format(avg_qr_time),'ns')
    print('Average time taken by Cholesky decomposition: ', '{:,}'.format(avg_cl_time),'ns')
    print('\nRatio LU:QR:CL ≈', round(lu_ratio), ':', round(qr_ratio), ':', round(cl_ratio))