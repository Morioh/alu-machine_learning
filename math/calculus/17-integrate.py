def poly_integral(poly, C=0):
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
print(poly_integral([5, 3, 0, 1], 0))  # Output should be [0, 5, 1.5, 0, 0.25]
print(poly_integral([3, 0, 1], 2))  # Output should be [2, 3, 0, 0.333...]
