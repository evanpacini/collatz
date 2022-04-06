// Collatz div2 steps percentage calculation with memoisation, openmp multithreading, bitwise operations (with reduced /2), and csv export

#define ull unsigned long long
#include <cstdio>
#include <fstream>

int main(int argc, char *argv[])
{
    ull N = strtoull(argv[1], NULL, 10);
    ull *steps = new ull[N + 2];
    long double *ps = new long double[N + 2];
    for (ull y = 0; y <= N; y++)
        ps[y] = steps[y] = 0;

#pragma omp parallel for
    for (ull i = 1; i <= N; i++)
    {
        ull n = i, c = 0;

        //3n+1
        while (n != 4)
        {
            n = 3 * n / (-n & n) + 1;
            c++;
        }

        // total
        ull n2 = i, c2 = 0;
        while (n2 != 1)
        {
            if (n2 < N && steps[n2])
            {
                c2 += steps[n2];
                break;
            }

            n2 = (n2 & 1) * ((n2 << 1) + 1 + n2) + !(n2 & 1) * (n2 >> 1); // unreadable but quick way of doing 3n+1
            c2++;
        }
        steps[i] = c2;
        ps[i] = (long double)(c2 - c + 1) / (long double)c2 * 100.0;
    }
    ps[4] = 0.0;

    //Export to csv
    std::ofstream csv("csv/collatzdiv2p.csv", std::ofstream::out);
    for (ull z = N / 10; z <= N; z += N / 10)
    {
        long double sum = 0;
        for (ull x = 2; x <= z; x++)
        {
            sum += ps[x];
            csv << x << "," << ps[x] << "\n";
        }
        csv.close();
        printf("SUM: %Lf; Average: %Lf\n", sum, sum / z);
    }
    //Cleanup
    delete[] ps;
    delete[] steps;

    return 0;
}