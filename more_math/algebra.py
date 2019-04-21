from math import factorial


class Algebra:
    """ Algebra class contains some mathematical functions like combinations, permutations etc"""

    @staticmethod
    def comb(n, r):
        """ Find the number of different combinations of 'r' identical items to be located in 'n' different places
         where n >= r. It is referred to as the combinatorial coefficient and is denoted by C = n! / (n - r)!r!. """

        if n < 0 or r < 0:
            raise ValueError("Enter non-negative integers")
        else:
            if n == r:
                return 1
            elif n == 0 or r == 0:
                return 1
            elif n <= r:
                raise ValueError("n should be greater or equal to r")
            else:
                diff_n_r = factorial(n - r)
                combination = factorial(n) / (diff_n_r * factorial(r))
                return combination
