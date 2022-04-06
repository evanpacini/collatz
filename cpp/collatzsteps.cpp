// Collatz steps calculation with memoisation, openmp multithreading, bitwise operations, and csv export

#include <cstdio>
#include <fstream>
#define ull unsigned long long

int main(int argc, char *argv[])
{
    ull N = strtoull(argv[1], NULL, 10);
    ull *steps = new ull[N + 1];
    for (ull i = 0; i <= N; i++)
    {
        steps[i] = 0;
    }
#pragma omp parallel for
    for (ull i = 2; i <= N; i++)
    {
        ull n = i, c = 0;
        while (n != 1)
        {
            if (n < N && steps[n])
            {
                c += steps[n];
                break;
            }

            n = (n & 1) * ((n << 1) + 1 + n) + !(n & 1) * (n >> 1); // unreadable but quick way of doing 3n+1
            c++;
        }
        steps[i] = c;

        // Pre-fill power-of-two multiples of this result
        for (n = i; n < N && !steps[i]; n *= 2)
        {
            steps[n] = c++;
        }
    }

    //Export to csv
    std::ofstream csv("csv/collatzsteps.csv", std::ofstream::out);
    for (ull i = 1; i <= N; i++)
    {
        csv << i << "," << steps[i] << "\n";
    }
    csv.close();

    //Cleanup
    delete[] steps;
    return 0;
}