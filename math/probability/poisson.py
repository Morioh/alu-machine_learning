#!/usr/bin/env python3

"""
Defines the Poisson class for Poisson distribution properties.

The Poisson distribution expresses the probability of a given number of events
occurring in a fixed interval, assuming a constant mean rate and independence
from the last event. This module allows initializing the distribution with data
or a specified mean rate (lambda) and computing the probability mass function
(PMF) for a given number of occurrences.

Classes:
    Poisson: Manages a Poisson distribution.
"""


class Poisson:
    """
    Represents a Poisson distribution, characterized by lambtha, the expected
    number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Poisson instance with data.
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

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes.

        Args:
            k (int): The number of successes.

        Returns:
            float: The PMF value for k.
        """
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        e = 2.7182818285
        lambtha_k_factorial = 1
        for i in range(1, k + 1):
            lambtha_k_factorial *= i

        pmf_value = (self.lambtha ** k) * \
            (e ** (-self.lambtha)) / lambtha_k_factorial
        return pmf_value
