import numpy as np

# Use Horner's method and calculate polynomial's derivative

def polynomial_value_and_derivative(coeffs, x):
    """
    coeffs 按幂次从高到低排列。
    返回P(x), P'(x)。
    """
    value = coeffs[0]
    derivative = 0
    
    for coefficient in coeffs[1:]:
        derivative = derivative*x + value
        value = value*x + coefficient

    return value, derivative

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g, g_prime = polynomial_value_and_derivative(g_coeffs, x)
    h, h_prime = polynomial_value_and_derivative(h_coeffs, x)

    if h == 0:
        raise ValueError("h(x) cannot be zero.")

    # f'(x) = [g'(x)h(x) - g(x)h'(x)]/[h(x)]^2

    return (g_prime*h - g*h_prime) / (h**2)
    
    