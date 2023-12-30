# Decomposition Analysis

## Introduction
Matrix decomposition methods, such as LU, QR, and Cholesky, play a pivotal role in various computational tasks, offering distinct approaches to break down matrices into simpler components. In this study, we investigate the computational efficiency of these methods by analyzing the average time required to decompose a matrix of size n. The aim is to discern the relative performance of LU, QR, and Cholesky decompositions

## Methods
LU,QR,Cholesky decomposition methods were implemented in Python with the help of the `Numpy` library. The average time required to decompose a matrix of size n was calculated by averaging the time required to decompose `m` randomly generated matrices of size `n`. The time required to decompose a matrix was calculated using the `timeit` library.  

## Libraries
- `Numpy`
- `timeit`
- `matplotlib`
- `csv`
## Results
The average time required to decompose a matrix of `size 1000` was calculated for `n = 10`. The results are shown in the table below.

| Method | Average Time (ns) |
| --- | --- |
| LU | 1329639190.0 ns |
| QR | 2652888460.0 ns |
| Cholesky | 1666343100.0 ns |

**`Ratio LU:QR:CL =  2 : 4 : 2`**

# Conclusion
The results show that the LU decomposition method is the fastest, followed by the Cholesky decomposition method, and then the QR decomposition method. The results also show that the QR decomposition method is twice as slow as the LU and Cholesky decomposition methods.
