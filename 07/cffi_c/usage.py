#! /usr/bin/env python

import cffi
import time

ROW = 100
COL = 90


def c_mul():
    ffi = cffi.FFI()
    lib = ffi.dlopen('./libmatrix.so')
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
    lib.c_mul_plenty_matr(matrix_even, matrix_odd, 500)
    end_ts = time.time()
    print(f"c_mul_matrix: {end_ts-start_ts}")


if __name__ == "__main__":
    c_mul()