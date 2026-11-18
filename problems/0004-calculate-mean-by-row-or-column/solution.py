import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    return np.mean(np.array(matrix), axis=0) if mode == 'column' else np.mean(np.array(matrix), axis=1)