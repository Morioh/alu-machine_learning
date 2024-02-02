def summation_i_squared(n):
    if not isinstance(n, int) or n <= 0:
        return None
    return n * (n + 1) * (2 * n + 1) // 6


# Example usage
print(summation_i_squared(5))  # Should return 14
print(summation_i_squared(-1))  # Should return None
