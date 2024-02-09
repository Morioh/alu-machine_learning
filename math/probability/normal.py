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

        Args:
            data (list, optional): Data to estimate the distribution.
            mean (float, optional): Mean of the distribution.
            stddev (float, optional): Standard deviation of the distribution.

        Raises:
            ValueError: If stddev is not positive or data contain many values.
            TypeError: If data is not a list.
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

            # Ensure mean and stddev are stored as floats
            self.mean = float(self.mean)
            self.stddev = float(self.stddev)
