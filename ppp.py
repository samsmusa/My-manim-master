import numpy as np
from manimlib import *


class NumericalMatrixMultiplication(Scene):
    CONFIG = {
        "left_matrix": [[1, 2], [3, 4]],
        "right_matrix": [[5, 6], [7, 8]],
        "use_parens": True,
    }

    def construct(self):
        left_string_matrix = np.array(self.left_matrix)
            # for matrix in (self.left_matrix, self.right_matrix)
        
        self.add(left_matrix)
        if right_string_matrix.shape[0] != left_string_matrix.shape[1]:
            raise Exception("Incompatible shapes for matrix multiplication")

        left = Matrix(left_string_matrix)
        right = Matrix(right_string_matrix)
        result = self.get_result_matrix(
            left_string_matrix, right_string_matrix
        )

        self.organize_matrices(left, right, result)
        self.animate_product(left, right, result)

   