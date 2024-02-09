#!/usr/bin/env python3
# poisson.py

"""
A module to represent and calculate properties of the Poisson distribution.

This module provides the Poisson class, which encapsulates the functionality
for representing a Poisson distribution. It includes methods for initializing
the distribution with either raw data or a specific lambda (λ) value, which
represents the expected number of occurrences within a given time frame.
"""


class Poisson:
    """
    Represents a Poisson distribution, characterized by lambtha, the expected
    number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson instance with data or a specific lambtha value.

        Args:
            data (list, optional): Data to estimate the distribution.
            lambtha (float, optional): Expected occurrences. Defaults to 1.

        Raises:
            ValueError: If lambtha <= 0 or data has < 2 values.
            TypeError: If data is not a list.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
