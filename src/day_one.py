"""day_one.py

"""

from AdventData import AdventData


def solve_p1():
    santa = AdventData.day_one

    floor = 0

    for x in santa:
        if x == '(':
            floor += 1
        if x == ')':
            floor -= 1

    return floor


def solve_p1_1():
    santa = AdventData.day_one

    return sum([1 if x is '(' else -1 for x in santa])


def solve_p1_2():
    return AdventData.day_one.count('(') - AdventData.day_one.count(')')


# === Part Two solutions
def solve_p2():
    santa = AdventData.day_one

    pos, floor = 0, 0

    while floor != -1:
        floor = floor + 1 if santa[pos] is '(' else floor - 1
        pos += 1

    return pos


def solve_p2_1():
    santa = AdventData.day_one

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
