#ifndef func_h
#define func_h

#include <iostream>
#include <chrono>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

template <typename Func, typename... Args>
std::pair<long long, decltype(std::declval<Func>()(std::declval<Args>()...))>

findTimeTaken(Func &&func, Args &&...args)
{
    auto start = std::chrono::high_resolution_clock::now();
    auto result = std::forward<Func>(func)(std::forward<Args>(args)...);
    auto stop = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start).count();
    return std::make_pair(duration, result);
}

std::string getFormattedTime(long long timeTaken)
{
    std::string formattedTime;
    if (timeTaken < 1000)
    {
        formattedTime = std::to_string(timeTaken) + " microseconds";
    }
    else if (timeTaken < 1000000)
    {
        formattedTime = std::to_string(timeTaken / 1000) + "." + std::to_string(timeTaken % 1000) + " milliseconds";
    }
    else
    {
        formattedTime = std::to_string(timeTaken / 1000000) + "." + std::to_string((timeTaken % 1000000) / 1000) + " seconds";
    }
    return formattedTime;
}

void compareAndSave( std::pair<long long, std::tuple<Matrix, Matrix>> timeTakenLU, std::pair<long long, std::tuple<Matrix, Matrix>> timeTakenQR, std::pair<long long, std::tuple<Matrix, Matrix>> timeTakenCL)
{
    std::ofstream file;
    
    file.open("asset/results.csv", std::ios::out | std::ios::app);
    if (file.is_open())
    {
        file << timeTakenLU.first << "," << timeTakenQR.first << "," << timeTakenCL.first << "\n";
    }
    else
    {
        std::cerr << " save Unable to open file: " << std::endl;
    }
    file.close();
}

void clearFile(std::string filename)
{
    std::ofstream file;
    file.open(filename, std::ios::out | std::ios::trunc);
    if (file.is_open())
    {
        file << "LU,QR,CL\n";
    }
    else
    {
        std::cerr << " clear Unable to open file: " << filename << std::endl;
    }
    file.close();
}

#endif