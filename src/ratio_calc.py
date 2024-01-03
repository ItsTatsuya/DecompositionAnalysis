import csv
import matplotlib.pyplot as plt
import numpy as np
import math

def read_results(filename):
    lu_times, qr_times, cl_times = [], [], []

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        for row in csv_reader:
            lu_times.append(int(row[0]))
            qr_times.append(int(row[1]))
            cl_times.append(int(row[2]))

    return lu_times, qr_times, cl_times

def ratio_calc():
    lu_times, qr_times, cl_times = read_results('asset/results.csv')

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
    
    print('\nAverage time taken by LU decomposition: {:,} ms'.format(avg_lu_time))
    print('Average time taken by QR decomposition: {:,} ms'.format(avg_qr_time))
    print('Average time taken by Cholesky decomposition: {:,} ms'.format(avg_cl_time))
    print('\nRatio LU:QR:CL ≈', round(lu_ratio), ':', round(qr_ratio), ':', round(cl_ratio))