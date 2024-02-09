#!/usr/bin/env python3

"""
This module provides the Exponential class for modeling and analyzing data
using the exponential distribution. It supports initializing the distribution
directly with a rate parameter (lambtha) or indirectly through data analysis.
The exponential distribution is useful in modeling the time between events
in a Poisson point process.

Classes:
    Exponential: Models an exponential distribution.
"""


class Exponential:
    """
    Represents an exponential distribution, characterized by the parameter
    lambtha, which is the expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initializes the Exponential instance with a specific lambtha value.

        Args:
            data (list, optional): Data to estimate the distribution.
            lambtha (float, optional): Expected number of occurrences.

        Raises:
            ValueError: If lambtha is not a positive value or data does not
                        contain multiple values.
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
            # Calculate lambtha as the reciprocal of the mean of the data
            self.lambtha = 1 / float(sum(data) / len(data))
