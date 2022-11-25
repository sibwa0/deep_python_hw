import unittest
import cffi

from mul_matrix import py_mul_plenty_matr


class TestMulMatr(unittest.TestCase):
    def test_py_mul(self):
        row = 5
        col = 10

        matrix_even = py_mul_plenty_matr(
            row,
            col,
            20
        )

        self.assertEqual(
            matrix_even.shape,
            (row, col)
        )

        matrix_odd = py_mul_plenty_matr(
            row,
            col,
            15
        )

        self.assertEqual(
            matrix_odd.shape,
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

        matrix_even = lib.create_matrix(COL, ROW)
        matrix_odd = lib.create_matrix(ROW, COL)
        lib.init_matrix_norm_value(matrix_even)
        lib.init_matrix_norm_value(matrix_odd)

        row = 5
        col = 10

        matrix_even = cffi_lib.c_mul_plenty_matr(row, col, 20)

        self.assertEqual(
            (matrix_even.row, matrix_even.col),
            (row, col)
        )

        matrix_odd = cffi_lib.c_mul_plenty_matr(row, col, 15)

        self.assertEqual(
            (matrix_odd.row, matrix_odd.row),
            (row, row)
        )
