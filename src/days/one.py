"""
--- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas, but his weather machine's "snow"
function is powered by stars, and he's fresh out! To save Christmas,
he needs you to collect *fifty stars* by December 25th.
"""

from AdventData import day_one


class PartOne:
    """
    Santa is trying to deliver presents in a large apartment building, but he
    can't find the right floor - the directions he got are a little
    confusing. He starts on the ground floor (floor 0) and then follows the
    instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing
    parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep; he
    will never find the top or bottom floors.

    For example:

      - (()) and ()() both result in floor 0.
      - ((( and (()(()( both result in floor 3.
      - ))((((( also results in floor 3.
      - ()) and ))( both result in floor -1 (the first basement level).
      - ))) and )())()) both result in floor -3.

    To what floor do the instructions take Santa?
    """
    @staticmethod
    def solve():
        santa = day_one

        floor = 0

        for x in santa:
            if x == '(':
                floor += 1
            if x == ')':
                floor -= 1

        return floor

    @staticmethod
    def solve_one():
        return sum([1 if x is '(' else -1 for x in day_one])

    @staticmethod
    def solve_two():
        return day_one.count('(') - day_one.count(')')


class PartTwo:
    """
    --- Part Two ---

    Now, given the same instructions, find the position of the first
    character that causes him to enter the basement (floor -1). The first
    character in the instructions has position 1, the second character has
    position 2, and so on.

    For example:

      - ) causes him to enter the basement at character position 1.
      - ()()) causes him to enter the basement at character position 5.

    What is the position of the character that causes Santa to first enter the basement?
    """
    @staticmethod
    def solve():
        santa = day_one
        pos, floor = 0, 0

        while floor != -1:
            floor = floor + 1 if santa[pos] is '(' else floor - 1
            pos += 1

        return pos

    @staticmethod
    def solve_one():
        santa = day_one

        pos, floor = 0, 0

        for x in santa:
            if x == '(':
                floor += 1
            else:
                floor -= 1
            pos += 1
            if floor == -1:
                return pos

        return pos + 1
