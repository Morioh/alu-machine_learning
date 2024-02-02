#!/usr/bin/env python3

"""
This module offers functionality for performing mathematical operations on
polynomials, with a focus on calculating their derivatives. It represents
polynomials as lists of coefficients, ordered by decreasing power.

The primary functionality is provided through the `poly_derivative` function,
which calculates a polynomial's derivative and returns the result in a similar
list format. This capability is essential for tasks in calculus and algebra,
making the module suitable for educational purposes, mathematical software
applications, and other contexts requiring polynomial calculus.

Details on using the `poly_derivative` function and examples are included within
the function's docstring, demonstrating the calculation of derivatives for
polynomials represented as lists of coefficients.
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial represented as a list of coefficients.

    The polynomial is assumed to be in the form of [a_n, a_{n-1}, ..., a_2, a_1, a_0],
    where a_n is the coefficient of the x^n term. The derivative is calculated based
    on standard calculus rules and returned as a list of coefficients in the same format.

    Parameters:
    - poly (list): A list of integers or floats representing the coefficients of a polynomial,
                   starting with the coefficient of the highest power of x.

    Returns:
    - list: A list of coefficients representing the derivative of the polynomial. If the
            input polynomial is constant or empty, returns [0]. Returns None if the input
            is not a list of numbers.

    Example Usage:
    >>> poly_derivative([5, 3, 0, 1])
    [3, 0, 3]
    >>> poly_derivative([3])
    [0]

    The first example corresponds to the derivative of 5x^3 + 3x^2 + 0x + 1, which is
    3x^2 + 0x + 3. The second example shows that the derivative of a constant (3) is 0.
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
