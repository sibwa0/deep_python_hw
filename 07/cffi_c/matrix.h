#ifndef CFFI_MATRIX_H_
#define CFFI_MATRIX_H_


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


#endif  // CFFI_MATRIX_H_
