# Import librarys
import numpy as np
from scipy.optimize import fsolve
import time
import sys
from intpy.intpy import initialize_intpy, deterministic
# Define parameters

T = 1
C = 1
Kd1 = 2
n2 = 1000
Kd2 = 1

# Use the numerical solver to find the roots
n_solutions = 200
x_list = np.linspace(1, 2e4, n_solutions)
F_list = np.empty_like(x_list)

@deterministic
def solve(n, F_solution):
    return fsolve(func=lambda x: n * C / (1 + Kd1 / x) + n2 * C / (1 + Kd2 / x) - T, x0=F_solution, xtol=1e-6)

@initialize_intpy(__file__)
def main(F_solution):
    for i in range(n_solutions):
        # Define function
        F_solution=solve(F_solution)
        F_list[i]=F_solution

        # Print result
        print('x: %20.8f \t\tF: %20.8f' % (x_list[i], F_solution))

if __name__ == '__main__':
    F_solution = float(sys.argv[1])
    start = time.perf_counter()
    main(F_solution)
    print(time.perf_counter() - start)
