#!/usr/bin/env python3

"""
This module defines the Binomial class for representing and analyzing data
using the binomial distribution. The binomial distribution describes the
number of successes in a fixed number of independent Bernoulli trials,
each with the same probability of success.

The Binomial class can be initialized directly with the number of trials
(n) and the probability of success (p), or it can estimate these parameters
from provided data. This flexibility makes the class useful for both
theoretical studies and practical data analysis where parameters are not
known a priori.

Classes:
    Binomial: Models a binomial distribution with methods to estimate
    parameters and calculate distribution properties.
"""


class Binomial:
    """
    Represents a binomial distribution, characterized by parameters n
    and p (probability of success).
    """

    def __init__(self, data=None, n=1, p=0.5):
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if not (0 < p < 1):
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.n = round(max(data))
            self.p = sum(data) / (len(data) * self.n)

    def factorial(self, num):
        """
        Computes factorial of num.

        Parameters:
            num (int): A non-negative integer.

        Returns:
            int: Factorial of num.
        """
        if num == 0 or num == 1:
            return 1
        else:
            return num * self.factorial(num - 1)

    def binomial_coefficient(self, n, k):
        """
        Computes binomial coefficient for (n, k).

        Parameters:
            n (int): Number of trials.
            k (int): Number of successes.

        Returns:
            float: Binomial coefficient.
        """
        return self.factorial(n) / (self.factorial(k) * self.factorial(n - k))

    def pmf(self, k):
        """
        Computes PMF for k successes in n trials.

        Parameters:
            k (int): Number of successes.

        Returns:
            float: PMF value.
        """
        k = int(k)  # Ensure k is an integer
        if k < 0 or k > self.n:
            return 0  # k is out of range

        binom_coeff = self.binomial_coefficient(self.n, k)
        pmf_value = binom_coeff * (self.p ** k) * \
            ((1 - self.p) ** (self.n - k))
        return pmf_value
