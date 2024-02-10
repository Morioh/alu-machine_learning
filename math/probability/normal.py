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
    Normal: Models a normal distribution with methods of statistical analysis.
"""


class Normal:
    """
    Represents a normal distribution.

    Attributes:
        mean (float): Mean of the distribution.
        stddev (float): Standard deviation of the distribution.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initializes the Normal instance either from data or given parameters.

        Parameters:
            data (list, optional): Data to estimate the distribution params.
            mean (float, optional): Mean of the distribution. Defaults to 0.
            stddev (float, optional): Standard deviation. Defaults to 1.

        Raises:
            ValueError: For invalid standard deviation values.
            TypeError: If data is not a list.
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean, self.stddev = float(mean), float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (
                sum((x - self.mean) ** 2 for x in data) / len(data)) ** 0.5

    def z_score(self, x):
        """Calculates the z-score of a given x-value."""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score."""
        return z * self.stddev + self.mean

    def pdf(self, x):
        """Calculates the PDF for a given x-value."""
        from math import exp, sqrt, pi
        return (1 / (self.stddev * sqrt(2 * pi))) * exp(-0.5 * ((x - self.mean) / self.stddev) ** 2)

    def cdf(self, x):
        """
        Calculates the CDF for a given x-value using a numerical approximation.
        """
        # Importing here to avoid global dependency
        from math import erf, sqrt

        # Utilizing the error function (erf) for CDF calculation
        return 0.5 * (1 + erf((x - self.mean) / (self.stddev * sqrt(2))))
