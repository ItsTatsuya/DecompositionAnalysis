#read the results.csv file and plot the graph, find the average time taken by each algorithm and plot the graph, and find the ratio of the average time taken by each algorithm and plot the graph.

import csv
import matplotlib.pyplot as plt
import numpy as np


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

    lu_ratio = round(avg_lu_time / avg_lu_time)
    qr_ratio = round(avg_qr_time / avg_lu_time)
    cl_ratio = round(avg_cl_time / avg_lu_time)

    x = ['LU', 'QR', 'CL']
    y = [lu_ratio, qr_ratio, cl_ratio]
    plot_graph(x, y, 'Comparison of Decomposition Algorithms', 'No of times run', 'time taken (nanoseconds)')

    print('Average time taken by LU decomposition: ', avg_lu_time,'ns')
    print('Average time taken by QR decomposition: ', avg_qr_time,'ns')
    print('Average time taken by Cholesky decomposition: ', avg_cl_time,'ns')

    print('Ratio LU:QR:CL = ', lu_ratio, ':', qr_ratio, ':', cl_ratio)