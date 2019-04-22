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

    @staticmethod
    def convert_denary_to_base(base, number):
        """ Returns a string representation of the number converted from base 10 (denary) to any base specified"""

        results = ""
        if base < 0 or number < 0:
            raise ValueError("Base or number can't be a negative integer")
        elif base in [0, 1]:
            raise ValueError("Base can't be below 2")
        else:
            base_16 = {10: "A", 11: "B", 12: "C", 13: "D",  14: "E", 15: "F"}
            if number == 0:
                return "1"
            elif number == 1:
                return "1"
            else:
                while number != 0:
                    if base == 16:
                        if number in base_16.keys():
                            results += base_16.get(number)
                            number //= base
                        elif (number % base) in base_16.keys():
                            results += base_16.get(number % base)
                            number //= base
                        else:
                            results += str(number % base)
                            number //= base
                    else:
                        results += str(number % base)
                        number //= base
                return results[::-1]

