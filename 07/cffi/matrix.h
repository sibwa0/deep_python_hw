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

Matrix* c_mul_plenty_matr(int row, int col, int iters);
Matrix* mul(const Matrix* l, const Matrix* r);


#endif  // CFFI_MATRIX_H_