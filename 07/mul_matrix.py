import numpy as np


def py_mul_plenty_matr(row: int, col: int, iters: int) -> np.ndarray:
    res = np.ones_like(np.arange(row * col).reshape(row, col))
    for i in np.arange(iters):
        if i % 2 == 0:
            res = res @ np.random.normal(0, 0.1, size=(col, row))
        else:
            res = res @ np.random.normal(0, 0.1, size=(row, col))

    return res
