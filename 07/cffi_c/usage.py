#! /usr/bin/env python

import cffi
import time


def c_mul():
    ffi = cffi.FFI()
    lib = ffi.dlopen('./lib_matrix.so')
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

    Matrix* c_mul_plenty_matr(int row, int col, int iters);
    int mul(const Matrix* l, const Matrix* r, Matrix* result);
    ''')
    matrix = ffi.new("Matrix *")

    start_ts = time.time()
    matrix = lib.c_mul_plenty_matr(90, 100, 500)
    end_ts = time.time()
    print(f"py_mul_matrix: {end_ts-start_ts}")
    print(matrix)

if __name__ == "__main__":
    c_mul()