#include "matrix.h"

#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <stdio.h>


Matrix* create_matrix(int row, int col)
{
    if (row == 0 || col == 0)
        return NULL;

    Matrix* matrix = malloc(sizeof(Matrix));

    if (matrix == NULL)
        return NULL;

    matrix->row = row;
    matrix->col = col;
    matrix->arr = calloc(row * col, sizeof(double));
    if (matrix->arr == NULL)
    {
        free(matrix);
        return NULL;
    }

    return matrix;
}

void init_matrix_norm_value(Matrix* matrix)
{
    srand(time(NULL));
    
    for (int i = 0; i < matrix->row; i += 1)
        for (int j = 0; j < matrix->col; j += 1)
            matrix->arr[i * matrix->col + j] = (double)rand() / RAND_MAX;
}

void init_ones_like(Matrix* matrix)
{
    for (int i = 0; i < matrix->row; i += 1)
        for (int j = 0; j < matrix->col; j += 1)
            matrix->arr[i * matrix->col + j] = 1;
}

void free_matrix(Matrix* matrix)
{
    if (matrix != NULL)
    {
        if (matrix->arr != NULL)
            free(matrix->arr);

        free(matrix);
    }
}

int not_enough_space(const Matrix* matrix) {
    if ((matrix == NULL) || (matrix->arr == NULL)) {
        return 1;
    }
    return 0;
}

int mul(const Matrix* l, const Matrix* r, Matrix* result) {
    if (not_enough_space(l) || not_enough_space(r)) {
        return 1;
    }
    if (l->col != r->row) {
        printf("wrong martixes size %d %d\n", l->col, r->row);
        return 1;
    }
    size_t l_rows = l->row;
    size_t l_cols = l->col;
    size_t r_cols = r->col;

    double l_elem = 0;
    double r_elem = 0;
    for (size_t i = 0; i < l_rows; i++) {
        for (size_t j = 0; j < r_cols; j++) {
            for (size_t k = 0; k < l_cols; k++) {
                l_elem = l->arr[i * l->col + k];
                r_elem = r->arr[k * r->col + j];
                result->arr[i * r_cols + j] += l_elem * r_elem;
            }
        }
    }
    return 0;
}

Matrix* c_mul_plenty_matr(Matrix* even_iter, Matrix* odd_iter, int iters)
{
    if (iters <= 0)
        return NULL;

    Matrix* res = create_matrix(even_iter->col, even_iter->row);
    for (int i = 0; i < res->row; i += 1)
        for (int j = 0; j < res->col; j += 1)
            res->arr[i * res->col + j] = 1;

    Matrix* tmp = create_matrix(odd_iter->row, odd_iter->row);

    for (int k = 0; k < iters; k += 1)
    {

        if (k % 2 == 0) {
            if (mul(res, even_iter, tmp))
            {
                printf("not mul even\n");
                return NULL;
            }
        }
        else
        {
            if (mul(tmp, odd_iter, res))
            {
                printf("not mul odd\n");
                return NULL;
            }
        }

        if (res == NULL)
        {
            printf("not res space\n");
            return NULL;
        }
    }

    if (iters % 2 != 0)
        return tmp;
    else
        return res;
}
