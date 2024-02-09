#!/usr/bin/env python3

"""
Module for representing and analyzing normal (Gaussian) distributions.

This module provides the Normal class to model normal distributions,
allowing for initialization with either raw data or specified mean and
standard deviation values. It supports basic statistical analysis on the
data, including calculating the distribution's mean and standard deviation
when given a dataset. The class is designed to handle cases where the
distribution parameters are directly provided or need to be estimated from
data, ensuring flexibility in statistical and probabilistic analysis.

Classes:
    Normal: Models a normal distribution with methods for statistical analysis.
"""


class Normal:
    """
    Represents a normal (Gaussian) distribution, characterized by the mean
    and standard deviation of the distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes the Normal instance with specific mean and stddev values.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (
                sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5

    def pdf(self, x):
        """
        Calculates the PDF value for a given x-value.
        """
        part1 = 1 / (self.stddev * (2 * 3.141592653589793) ** 0.5)
        exponent = -0.5 * (((x - self.mean) / self.stddev) ** 2)
        part2 = 2.718281828459045 ** exponent
        return part1 * part2

    def cdf(self, x):
        """
        Calculates the CDF value for a given x-value using a basic approximation.
        """
        # Constants for Abramowitz and Stegun approximation
        a1 = 0.254829592
        a2 = -0.284496736
        a3 = 1.421413741
        a4 = -1.453152027
        a5 = 1.061405429
        p = 0.3275911

        # Change of variable
        sign = 1 if x >= self.mean else -1
        z = abs(x - self.mean) / (self.stddev * (2 ** 0.5))

        # Abramowitz and Stegun approximation for error function
        t = 1 / (1 + p * z)
        erf_approx = 1 - (((((a5 * t + a4) * t) + a3) * t + a2)
                          * t + a1) * t * (2.718281828459045 ** (-z * z))

        return 0.5 * (1 + sign * erf_approx)
