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

            # Calculate p as the total successes divided by the total #trials
            total_successes = sum(data)
            total_trials = len(data) * max(data)  # Estimate of total trials
            self.p = total_successes / total_trials

            # Assume each data point a success count for a fixed #trials
            # Average success rate to estimate p directly, then estimating n
            average_successes = total_successes / len(data)
            # Use the highest success count as an estimate for n
            self.p = average_successes / max(data)
            # Assuming the max value in data approximates n
            self.n = round(max(data))

            # Recalculate p using the newly estimated n for a better estimate
            self.p = total_successes / (self.n * len(data))
