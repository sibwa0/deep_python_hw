#! /usr/bin/env python

import time
import cffi

from mul_matrix import py_mul_plenty_matr

RAW = 75
COL = 100
ITERS = 700


def main():
    print("=== Python ===")
    start_ts = time.time()
    py_mul_plenty_matr(RAW, COL, ITERS)
    end_ts = time.time()
    print(f"py_mul_plenty_matr: {end_ts-start_ts}")

    print("==== cffi ====")
    ffi = cffi.FFI()
    cffi_lib = ffi.dlopen('./cffi_c/lib_matrix.so')
    ffi.cdef('''
    typedef struct Matrix {
        int row;
        int col;
        double* arr;
    } Matrix;

    Matrix* c_mul_plenty_matr(int row, int col, int iters);
    ''')
    # matrix = ffi.new("Matrix *")

    start_ts = time.time()
    cffi_lib.c_mul_plenty_matr(RAW, COL, ITERS)
    end_ts = time.time()
    print(f"c_mul_plenty_matr: {end_ts-start_ts}")


if __name__ == "__main__":
    main()
