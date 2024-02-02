#!/usr/bin/env python3

def poly_integral(poly, C=0):
    """
    Calculate the integral of a polynomial represented as a list of coefficients,
    with an optional constant of integration.

    The polynomial is assumed to be in the form [a_n, a_{n-1}, ..., a_2, a_1, a_0],
    where a_n is the coefficient of the x^n term. The integral is calculated based
    on standard calculus rules and returned as a list of coefficients in the same
    format, with the constant of integration as the first term.

    Parameters:
    - poly (list): A list of integers or floats representing the coefficients of
                   a polynomial, starting with the coefficient of the highest power of x.
    - C (int, float, optional): The constant of integration. Defaults to 0.

    Returns:
    - list: A list of coefficients representing the integral of the polynomial.
            If the input list is empty, returns a list containing only the constant of integration.
            Returns None if the inputs are not valid (i.e., poly is not a list of numbers or C is not a number).

    Example Usage:
    >>> poly_integral([5, 3, 0, 1], 0)
    [0, 5, 1.5, 0, 0.25]
    >>> poly_integral([3, 0, 1], 2)
    [2, 3, 0, 0.333...]

    The first example corresponds to the integral of 5x^3 + 3x^2 + 0x + 1 with a constant of integration 0,
    resulting in 5x^4/4 + 3x^3/3 + 0x^2/2 + x + 0. The coefficients are returned as [0, 5, 1.5, 0, 0.25].
    The second example shows the integral of 3x^2 + 0x + 1 with a constant of integration 2.
    """

    # Check if poly and C are valid
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly) or not isinstance(C, (int, float)):
        return None

    # Check if the polynomial is empty
    if not poly:
        return [C] if isinstance(C, int) else [float(C)]

    # Calculate the integral
    integral = [C] + [coef / (i + 1) for i, coef in enumerate(poly)]

    # Convert to integer if possible, ensuring coef is treated as a float before checking is_integer()
    integral = [int(coef) if isinstance(coef, float)
                and coef.is_integer() else coef for coef in integral]

    return integral


# Example usage
# print(poly_integral([5, 3, 0, 1], 0))  # Output should be [0, 5, 1.5, 0, 0.25]
# print(poly_integral([3, 0, 1], 2))  # Output should be [2, 3, 0, 0.333...]
