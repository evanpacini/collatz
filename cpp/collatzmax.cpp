// Collatz peak calculation with memoisation, openmp multithreading, bitwise operations, and csv export

#include <cstdio>
#include <cstdlib>
#include <fstream>
#define ull unsigned long long

int main(int argc, char *argv[])
{
    ull N = strtoull(argv[1], NULL, 10);
    ull *peaks = new ull[N + 1];
    for (ull i = 0; i <= N; i++)
    {
        peaks[i] = 1;
    }
#pragma omp parallel for
    for (ull i = 1; i <= N; i++)
    {
        ull n = i;
        while (n != 1)
        {
            peaks[i] = peaks[i] + (n > peaks[i]) * (n - peaks[i]);  // if n > max => max = n
            n = (n & 1) * ((n << 1) + 1 + n) + !(n & 1) * (n >> 1); // unreadable but quick way of doing 3n+1
        }
    }

    //Export to csv
    std::ofstream csv("csv/collatzmax.csv", std::ofstream::out);
    for (ull i = 1; i <= N; i++)
    {
        csv << i << "," << peaks[i] << "\n";
    }
    csv.close();

    //Cleanup
    delete[] peaks;
    return 0;
}