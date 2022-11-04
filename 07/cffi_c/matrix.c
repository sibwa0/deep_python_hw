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

    result->row = l_rows;
    result->col = r_cols;

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

Matrix* c_mul_plenty_matr(int row, int col, int iters)
{
    Matrix* res = create_matrix(row, col);
    for (int i = 0; i < row; i += 1)
        for (int j = 0; j < col; j += 1)
            res->arr[i * col + j] = 1;

    Matrix* even_iter = create_matrix(col, row);
    Matrix* odd_iter = create_matrix(row, col);

    Matrix* tmp = NULL;

    for (int k = 0; k < iters; k += 1)
    {
        tmp = res;

        if (k % 2 == 0) {
            init_matrix_norm_value(even_iter);
            if (mul(tmp, even_iter, res))
            {
                printf("not mul even\n");
                return NULL;
            }
        }
        else
        {
            init_matrix_norm_value(odd_iter);
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

    free_matrix(even_iter);
    free_matrix(odd_iter);

    return res;
}
