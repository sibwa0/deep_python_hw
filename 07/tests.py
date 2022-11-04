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
