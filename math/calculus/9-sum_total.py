#!/usr/bin/env python3

def summation_i_squared(n):
    """
    Calculate the sum of the squares of the first n positive integers.

    This function uses the formula:
        sum(i^2 for i in range(1, n+1)) = n(n + 1)(2n + 1) / 6

    Parameters:
    - n (int): The number of initial positive integers to include in the sum.

    Returns:
    - int or None: The sum of the squares of the first n positive integers if n is a positive integer.
      Returns None if n is not an integer or is less than or equal to 0.

    Example Usage:
    >>> summation_i_squared(5)
    55
    >>> summation_i_squared(-1)
    None
    """

    if not isinstance(n, int) or n <= 0:
        return None
    return n * (n + 1) * (2 * n + 1) // 6


# Example usage
# print(summation_i_squared(5))  # Should return 55
# print(summation_i_squared(-1))  # Should return None
