import numpy as np
from typing import List, Tuple
from matplotlib import pyplot as plt

def func_py(x: float) -> float:
    """
    Calculate function values for passed argument
    """
    N = 1  # Define N (assuming it's a constant)
    alpha = 2  # Define alpha (assuming it's a constant)
    return N * (x / N + 1/2) ** alpha - N/2

def tabulate_py(a: float, b: float, n: int) -> Tuple[List[float], List[float]]:
    x = [a + x*(b - a)/n for x in range(n)]
    y = [func_py(xi) for xi in x]
    return x, y

def tabulate_np(a: float, b: float, n: int) -> Tuple[np.ndarray, np.ndarray]:
    x = np.linspace(a, b, n)
    y = func_py(x)
    return x, y

def test_tabulation(f, a, b, n, axis):
    res = f(a, b, n)
    axis.plot(res[0], res[1])
    axis.grid()

def main():
    a, b, n = 0, 1, 1000

    fig, (ax1, ax2) = plt.subplots(2, 1)
    test_tabulation(tabulate_py, a, b, n, ax1)
    test_tabulation(tabulate_np, a, b, n, ax2)
    plt.show()

if __name__ == '__main__':
    main()