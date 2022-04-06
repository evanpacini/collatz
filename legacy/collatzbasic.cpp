// Basic Collatz steps calculation

#include <cstdio>
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
    for (ull i = 1; i <= N; i++)
    {
        ull n = i, c = 0;
        while (n != 1)
        {
            n = (n & 1) * (3 * n + 1) + !(n & 1) * (n / 2); // if n is odd 3n + 1 else n /= 2
            c++;
        }
        steps[i] = c;

        // Keep track of maximum step counts
        max = max + (c > max) * (c - max);     // if c > max => max = c
        imax = imax + (c == max) * (i - imax); //            => imax = i
    }
    printf("\nDone!\nMax step count is at seed %llu (%llu).\n", imax, steps[imax]);
    delete[] steps;
    return 0;
}