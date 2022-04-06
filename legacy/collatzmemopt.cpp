// Collatz steps calculation with memoisation, openmp multithreading and csv export

#include <cstdio>
#include <fstream>
#define ull unsigned long long

int main()
{
    ull N, imax, max = 0;
    printf("N: ");
    scanf("%llu", &N);
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

            n = (n & 1) * (3 * n + 1) + !(n & 1) * (n / 2); // if n is odd 3n + 1 else n /= 2
            c++;
        }
        steps[i] = c;

        // Keep track of maximum step counts
        max = max + (c > max) * (c - max);     // if c > max => max = c
        imax = imax + (c == max) * (i - imax); //            => imax = i

        // Pre-fill power-of-two multiples of this result
        for (n = i; n < N && !steps[i]; n *= 2)
        {
            steps[n] = c++;
        }
    }
    printf("\nDone!\nMax step count is at seed %llu (%llu).\n", imax, steps[imax]);

    //Export to csv
    std::ofstream csv("collatzsteps.csv", std::ofstream::out);
    for (ull i = 1; i <= N; i++)
    {
        csv << i << "," << steps[i] << "\n";
    }
    csv.close();

    //Cleanup
    delete[] steps;
    return 0;
}