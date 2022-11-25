#! /usr/bin/env python

import time
import cffi

from mul_matrix import py_mul_plenty_matr

ROW = 90
COL = 100
ITERS = 500


def main():
    print("=== Python ===")
    start_ts = time.time()
    py_mul_plenty_matr(ROW, COL, ITERS)
    end_ts = time.time()
    print(f"py_mul_plenty_matr: {end_ts-start_ts}")

    print("==== cffi ====")
    ffi = cffi.FFI()
    lib = ffi.dlopen('./cffi_c/libmatrix.so')
    ffi.cdef('''
    typedef struct Matrix {
        int row;
        int col;
        double* arr;
    } Matrix;

    Matrix* create_matrix(int row, int col);
    void init_matrix_norm_value(Matrix* matrix);
    void free_matrix(Matrix* matrix);
    int not_enough_space(const Matrix* matrix);

    Matrix* c_mul_plenty_matr(Matrix* even_iter, Matrix* odd_iter, int iters);
    int mul(const Matrix* l, const Matrix* r, Matrix* result);
    ''')

    matrix_even = lib.create_matrix(COL, ROW)
    matrix_odd = lib.create_matrix(ROW, COL)
    lib.init_matrix_norm_value(matrix_even)
    lib.init_matrix_norm_value(matrix_odd)


    start_ts = time.time()
    lib.c_mul_plenty_matr(matrix_even, matrix_odd, ITERS)
    end_ts = time.time()
    print(f"c_mul_matrix: {end_ts-start_ts}")


if __name__ == "__main__":
    main()
