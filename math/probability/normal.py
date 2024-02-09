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
        Initializes the Normal instance with data or specific mean and stddev values.
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

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.

        Args:
            x (float): The x-value.

        Returns:
            float: The z-score of x.
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.

        Args:
            z (float): The z-score.

        Returns:
            float: The x-value of z.
        """
        return self.mean + z * self.stddev
