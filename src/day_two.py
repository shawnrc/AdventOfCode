"""

"""

from AdventData import AdventData


def solve_p1() -> int:
    boxes = AdventData.day_two.split('\n')

    areas = []
    for box in boxes:
        l, w, h = dims = [int(x) for x in box.split('x')]
        area = (2 * l * w) + (2 * w * h) + (2 * h * l)
        dims.sort()
        areas.append(area + dims[0] * dims[1])

    return sum(areas)


def solve_p2() -> int:
    """
    --- Part Two ---

    The elves are also running low on ribbon. Ribbon is all the same width,
    so they only have to worry about the length they need to order, which
    they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its
    sides, or the smallest perimeter of any one face. Each present also
    requires a bow made out of ribbon as well; the feet of ribbon required
    for the perfect bow is equal to the cubic feet of volume of the present.
    Don't ask how they tie the bow, though; they'll never tell.

    For example:

      - A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon
        to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a
        total of 34 feet.
      - A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon
        to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a
        total of 14 feet.

    How many total feet of ribbon should they order?

    Solution: 3842356
    """

    boxes = [[int(d) for d in box.split('x')] for box in AdventData.day_two.split('\n')]  # hnngh list comprehensions

    ribbon = 0
    for box in boxes:
        box.sort()
        ribbon += 2 * sum(box[:2]) + box[0] * box[1] * box[2]

    return ribbon


print("Part 1: {}".format(solve_p1()))
print("Part 2: {}".format(solve_p2()))
