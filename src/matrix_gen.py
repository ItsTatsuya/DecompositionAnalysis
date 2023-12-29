import numpy as np
import csv

def generate(size, filename):
    A = np.random.randint(0, 10, size=(size, size))
    symmetric_matrix = (A + A.T) // 2
    spd_matrix = symmetric_matrix @ symmetric_matrix.T + np.eye(size) * 0.1  # Adding a small diagonal perturbation

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(spd_matrix)
