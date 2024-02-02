def poly_derivative(poly):
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
print(poly_derivative([5, 3, 0, 1]))
# Output should be [0], because the derivative of a constant is 0
print(poly_derivative([3]))
