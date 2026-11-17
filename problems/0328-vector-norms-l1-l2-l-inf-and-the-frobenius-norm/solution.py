import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    norm_type_dict = {"l1": 1, "l2": 2, "linf": np.inf, "frobenius": "fro"}
    if norm_type not in norm_type_dict:
        raise ValueError
    elif norm_type == "frobenius" and arr.ndim == 1:
        raise ValueError
    elif arr.ndim != 1 and arr.ndim != 2:
        raise ValueError
    else:
        if norm_type != "frobenius" and arr.ndim == 2:
            arr = arr.ravel()
        return float(np.linalg.norm(arr, norm_type_dict[norm_type]))
