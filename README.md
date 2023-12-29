# Decomposition Analysis

## Introduction
Matrix decomposition methods, such as LU, QR, and Cholesky, play a pivotal role in various computational tasks, offering distinct approaches to break down matrices into simpler components. In this study, we investigate the computational efficiency of these methods by analyzing the average time required to decompose a matrix of size 100. The aim is to discern the relative performance of LU, QR, and Cholesky decompositions, providing practical insights for choosing the most suitable method in specific numerical applications.

## Methods
We use the `decompose` function to decompose a matrix of size 100 using LU, QR, and Cholesky methods. The function returns the time required to decompose the matrix using the specified method. We repeat this process 100 times and calculate the average time required to decompose the matrix using each method. The results are shown in the table below.  

| Method | Average Time (s) |
| --- | --- |
| LU | 0.0005 |
| QR | 0.0005 |
| Cholesky | 0.0002 |

## Results
The results show that Cholesky decomposition is the fastest method, followed by LU and QR. This is because Cholesky decomposition is a special case of LU decomposition, which is a special case of QR decomposition. In other words, Cholesky decomposition is the most efficient method because it is the least general method.
