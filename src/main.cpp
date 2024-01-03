#include <iostream>
#include "decomp.h"
#include "func.h"
using std::cout, std::endl, std::cin, std::tie;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        std::cerr << "Usage: " << argv[0] << " size" << std::endl;
        return 1;
    }

    int size = std::stoi(argv[1]);
    std::pair<long long, std::tuple<Matrix, Matrix>> timeTakenLU, timeTakenQR, timeTakenCL;
    std::string fileName = "asset/matrix.csv";
    Matrix A(fileName);
    try
    {
        clearFile("asset/results.csv");
        cout << "Calculating..."<<endl;
        for (int i = 0; i < size; i++)
        {
            timeTakenLU = findTimeTaken(LUDecomposition, A);
            timeTakenQR = findTimeTaken(QRDecomposition, A);
            timeTakenCL = findTimeTaken(CLDecomposition, A);
            compareAndSave(timeTakenLU, timeTakenQR, timeTakenCL);
            cout << "Progress : " << i + 1 << "/" << size << endl;
        }
    }
    catch (const std::exception &e)
    {
        cout << "Error : " << e.what() << endl;
    }
    return 0;
}