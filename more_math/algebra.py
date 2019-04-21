from math import factorial


class Algebra:
    """ Algebra class contains some mathematical functions like combinations, permutations etc"""

    @staticmethod
    def comb(n, r):
        """ Returns the number of different combinations of 'r' identical items to be located in 'n' different places
         where n >= r. """

        if n < 0 or r < 0:
            raise ValueError("Enter non-negative integers")
        else:
            if n < r:
                raise ValueError("n should be greater or equal to r")
            elif r == 0 or n == r:
                return 1
            else:
                diff_n_r = factorial(n - r)
                combination = factorial(n) / (diff_n_r * factorial(r))
                return combination

    @staticmethod
    def perm(n, r):
        """ Returns the number of ordered combinations of 'n' objects taken 'r' at a time."""

        if n < 0 or r < 0:
            raise ValueError("Enter non-negative integers")
        else:
            if n < r:
                raise ValueError("n should be greater or equal to r")
            else:
                diff_n_r = factorial(n - r)
                permutation = factorial(n) / diff_n_r
                return permutation
