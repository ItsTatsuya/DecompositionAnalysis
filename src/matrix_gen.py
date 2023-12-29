import numpy as np
import csv

def generate(size, filename):
    A = np.random.randint(0, 10, size=(size, size))
    symmetric_matrix = (A + A.T) // 2
    spd_matrix = symmetric_matrix @ symmetric_matrix.T

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in spd_matrix:
            writer.writerow(row)
