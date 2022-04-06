// Collatz 3n+1 steps calculation with memoisation, openmp multithreading, bitwise operations (with reduced /2), and csv export

#define ull unsigned long long
#include <cstdio>
#include <fstream>

int main(int argc, char *argv[])
{
    ull N = strtoull(argv[1], NULL, 10);
    ull *steps = new ull[N + 1];
    for (ull i = 0; i <= N; i++)
    {
        steps[i] = 0;
    }

#pragma omp parallel for
    for (ull i = 1; i <= N; i++)
    {
        ull n = i, c = 0;
        while (n != 4)
        {
            n = 3 * n / (-n & n) + 1;
            c++;
        }
        steps[i] = c - 1;
    }
    steps[4] = 0;

    //Export to csv
    std::ofstream csv("csv/collatz3n+1steps.csv", std::ofstream::out);
    for (ull i = 1; i <= N; i++)
    {
        csv << i << "," << steps[i] << "\n";
    }
    csv.close();

    //Cleanup
    delete[] steps;

    return 0;
}