#! /usr/bin/env python3
"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as
gifts for all the economically forward-thinking little girls and boys.
"""

from AdventData import day_four
import hashlib


class PartOne:
    """
    To do this, he needs to find MD5 hashes which, in hexadecimal, start with
    at least five zeroes. The input to the MD5 hash is some secret key (your
    puzzle input, given below) followed by a number in decimal. To mine
    AdventCoins, you must find Santa the lowest positive number (no leading
    zeroes: 1, 2, 3, ...) that produces such a hash.
    """
    @staticmethod
    def solve(key=day_four, zeroes=5):
        count = 0
        while hashlib.md5(bytes(key + str(count), 'utf-8')).hexdigest()[:zeroes] != '0' * zeroes:
            count += 1
        return count


class PartTwo:
    """
    --- Part Two ---

    Now find one that starts with six zeroes.
    """
    @staticmethod
    def solve(key=day_four):
        return PartOne.solve(key, 6)

print(PartOne.solve())
#print(PartTwo.solve())
print("abcdef: {}".format(PartOne.solve("abcdef")))
