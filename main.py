from src.matrix_gen import generate
from src.ratio_calc import ratio_calc
import csv
import subprocess

cpp_file = 'src/main.cpp'
compile_command = ['g++', cpp_file, '-o', 'output_executable']
subprocess.run(compile_command, check=True)

def main():
    # Generating the matrix
    matrix_size = int(input('Enter the size of the matrix: '))
    size = input('Enter the number of times you want to run the algorithms: ')
    file_name = 'asset/matrix.csv'
    generate(matrix_size, file_name)

    # Run the compiled executable
    executable_command = ['./output_executable',size]
    subprocess.run(executable_command,check=True)
    
    ratio_calc()

if __name__ == '__main__':
    main()