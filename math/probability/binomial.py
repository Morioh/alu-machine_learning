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

            # Calculate p as the average number of successes per trial
            # Assume each entry in data represents the successes in a trial
            successes = sum(data)
            # Estimate total trials based on maximum successes observed
            trials = len(data) * max(data)
            self.p = successes / trials  # Initial estimate for p

            # Estimate n as the total number of trials (rounded)
            self.n = round(trials / max(data))

            # Recalculate p using the newly estimated n
            self.p = successes / (self.n * len(data))
