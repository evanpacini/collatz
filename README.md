# Warning: As of the 6th of April 2022, this readme is not up to date!

# Collatz

Multiple C++ and and Python programs to analyse the Collatz problem.

# Legacy README

## Collatz

C++ program that counts the number of steps to get back to 1 for all numbers up to N and saves it to a csv file.
Python program that imports the csv file and plots the number of steps vs seed using matplotlib.

### C++ program versions

- collatzbasic.cpp (the first version I made, just calculates all sequences up to N, and returns the seed with the highest number of steps)
- collatzmem.cpp (the same as the basic one, except it uses memoisation to significantly speed up the process)
- collatzmemopt.cpp (uses memoisation and OpenMP multithreading to speed up, exports results to collatzsteps.csv)
- collatzmemoptbin.cpp (same as previous except for small optimisations such as the use of bitwise operators)

Attention: the collatzmemopt.cpp and collatzmemoptbin.cpp require OpenMP to work efficiently... This can be done by using:

- `$ g++ -o collatz -fopenmp collatzmemoptbin.cpp` for GNU-based compilers
- `$ icl -o collatz /MD /Qopenmp collatzmemoptbin.cpp` for Intel compilers

### Python program

Will import collatzsteps.csv and plot it with matplotlib. matplotlib and csv libraries are required and can be installed using:

- `$ pip install matplotlib csv`
