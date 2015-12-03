"""

"""

from AdventData import AdventData


def solve_p1():
    boxes = AdventData.day_two.split('\n')

    areas = []
    for box in boxes:
        l, w, h = dims = [int(x) for x in box.split('x')]
        area = (2 * l * w) + (2 * w * h) + (2 * h * l)
        dims.sort()
        areas.append(area + dims[0] * dims[1])

    return sum(areas)
