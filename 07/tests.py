import unittest
import cffi
import numpy as np

from mul_matrix import py_mul_plenty_matr


class TestMulMatr(unittest.TestCase):
    def test_py_mul(self):
        row = 5
        col = 10
        even = np.random.normal(0, 0.1, size=(col, row))
        odd = np.random.normal(0, 0.1, size=(row, col))

        matrix_even_res = py_mul_plenty_matr(
            even,
            odd,
            20
        )

        self.assertEqual(
            matrix_even_res.shape,
            (row, col)
        )

        matrix_odd_res = py_mul_plenty_matr(
            even,
            odd,
            15
        )

        self.assertEqual(
            matrix_odd_res.shape,
            (row, row)
        )

    def test_c_mul(self):
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

        row = 5
        col = 10

        matrix_even = lib.create_matrix(col, row)
        matrix_odd = lib.create_matrix(row, col)
        lib.init_matrix_norm_value(matrix_even)
        lib.init_matrix_norm_value(matrix_odd)

        matrix_even_res = lib.c_mul_plenty_matr(matrix_even, matrix_odd, 20)

        self.assertEqual(
            (matrix_even_res.row, matrix_even_res.col),
            (row, col)
        )

        matrix_odd_res = lib.c_mul_plenty_matr(matrix_even, matrix_odd, 15)

        self.assertEqual(
            (matrix_odd_res.row, matrix_odd_res.row),
            (row, row)
        )

    def test_result_value_even(self):
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
        void init_ones_like(Matrix* matrix);
        void free_matrix(Matrix* matrix);
        int get_elem(Matrix* matrix, int row, int col);
        int not_enough_space(const Matrix* matrix);

        Matrix* c_mul_plenty_matr(Matrix* even_iter, Matrix* odd_iter, int iters);
        int mul(const Matrix* l, const Matrix* r, Matrix* result);
        ''')

        row = 2
        col = 3
        iters = 2

        even_c = lib.create_matrix(col, row)
        odd_c = lib.create_matrix(row, col)
        lib.init_ones_like(even_c)
        lib.init_ones_like(odd_c)

        matrix_even_res_c = lib.c_mul_plenty_matr(
            even_c, odd_c, iters
        )

        tmp_c = lib.create_matrix(row, col)
        lib.init_ones_like(tmp_c)

        for i in range(row):
            for j in range(col):
                self.assertTrue(
                    tmp_c.arr[i * tmp_c.col + j] * 6
                    == matrix_even_res_c.arr[i * tmp_c.col + j] - 1
                )

        even_py = np.ones_like(np.arange(row * col).reshape(col, row))
        odd_py = np.ones_like(np.arange(row * col).reshape(row, col))

        matrix_even_res_py = py_mul_plenty_matr(
            even_py, odd_py, iters
        )

        self.assertTrue(
            (matrix_even_res_py ==
            np.ones_like(np.arange(row * col).reshape(row, col)) * 6).all()
        )

    def test_result_value_odd(self):
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
        void init_ones_like(Matrix* matrix);
        void free_matrix(Matrix* matrix);
        int get_elem(Matrix* matrix, int row, int col);
        int not_enough_space(const Matrix* matrix);

        Matrix* c_mul_plenty_matr(Matrix* even_iter, Matrix* odd_iter, int iters);
        int mul(const Matrix* l, const Matrix* r, Matrix* result);
        ''')

        row = 2
        col = 3
        iters = 1

        even_c = lib.create_matrix(col, row)
        odd_c = lib.create_matrix(row, col)
        lib.init_ones_like(even_c)
        lib.init_ones_like(odd_c)

        matrix_even_res_c = lib.c_mul_plenty_matr(
            even_c, odd_c, iters
        )

        tmp_c = lib.create_matrix(row, row)
        lib.init_ones_like(tmp_c)

        for i in range(row):
            for j in range(row):
                self.assertTrue(
                    tmp_c.arr[i * tmp_c.col + j] * 3
                    == matrix_even_res_c.arr[i * tmp_c.col + j]
                )

        even_py = np.ones_like(np.arange(row * col).reshape(col, row))
        odd_py = np.ones_like(np.arange(row * col).reshape(row, col))

        matrix_even_res_py = py_mul_plenty_matr(
            even_py, odd_py, iters
        )

        self.assertTrue(
            (matrix_even_res_py ==
            np.ones_like(
                np.arange(row * row).reshape(row, row)
            ) * 3).all()
        )
