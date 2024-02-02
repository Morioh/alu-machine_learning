#!/usr/bin/env python3

"""
Provides functionality for mathematical operations on polynomials, notably 
calculating derivatives. Polynomials are represented as lists of coefficients 
in descending power order.

The `poly_derivative` function is the core feature, computing the derivative 
of a given polynomial and returning it in list format. This function is 
crucial for calculus and algebra tasks, making the module ideal for educational 
use, mathematical software development, and other areas needing polynomial 
calculus.

For usage details and examples of the `poly_derivative` function, including 
how to compute derivatives for polynomials represented by coefficient lists, 
refer to the function's docstring.
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial represented as a list of coefficients.

    Polynomials are given in the form [a_n, a_{n-1}, ..., a_2, a_1, a_0], where
    a_n is the coefficient for the x^n term. The derivative is computed using
    standard calculus rules and is returned as a list in the same format.

    Parameters:
    - poly (list): List of integers or floats as coefficients of the polynomial,
    starting with the highest power of x.

    Returns:
    - list: Coefficients list of the polynomial's derivative. Returns [0] if the
    input polynomial is constant or empty. Returns None if the input is not a
    list of numbers.

    Example Usage:
    >>> poly_derivative([5, 3, 0, 1])
    [3, 0, 3]
    >>> poly_derivative([3])
    [0]

    The first example shows the derivative of 5x^3 + 3x^2 + 0x + 1 as 3x^2 + 0x + 3.
    The second example demonstrates that the derivative of a constant (3) is 0.
    """

    # Check if poly is valid
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    # Check if the polynomial is a constant or empty, derivative is 0
    if len(poly) <= 1:
        return [0]

    # Calculate the derivative
    derivative = [i * coef for i, coef in enumerate(poly) if i > 0]

    return derivative


# Example usage
# Output should be [3, 0, 3], which corresponds to 3x^2 + 0x + 3
# print(poly_derivative([5, 3, 0, 1]))
# Output should be [0], because the derivative of a constant is 0
# print(poly_derivative([3]))
