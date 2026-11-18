import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    tr = np.trace(matrix)
    det = np.linalg.det(matrix)
    delta = tr**2-4*det
    if delta >= 0:
        return [-(-tr-np.sqrt(delta))/2, -(-tr+np.sqrt(delta))/2]
    # elif delta == 0:
    #     return [tr/2]
    # return eigenvalues