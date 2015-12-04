#!/usr/bin/env python3
"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.
"""

from AdventData import day_three


class PartOne:
    """
    He begins by delivering a present to the house at his starting location, and
    then an elf at the North Pole calls him via radio and tells him where to move
    next. Moves are always exactly one house to the north (^), south (v), east (>),
    or west (<). After each move, he delivers another present to the house at his
    new location.

    However, the elf back at the north pole has had a little too much eggnog, and
    so his directions are a little off, and Santa ends up visiting some houses more
    than once. How many houses receive *at least one present*?

    For example:

      - > delivers presents to 2 houses: one at the starting location, and one
      to the east.
      - ^>v< delivers presents to 4 houses in a square, including twice to the
      house at his starting/ending location.
      - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at
      only 2 houses.

    Solution: 2565
    """
    @staticmethod
    def solve(path=day_three):
        """
        This is going to be kind of a naive solution - maybe I'll store coordinates and check if
        I've visited before?
        """
        houses = 1
        x = y = 0
        visited = [(0, 0)]

        for move in path:

            if move is '^':
                y += 1
            elif move is '>':
                x += 1
            elif move is 'v':
                y -= 1
            elif move is '<':
                x -= 1

            pos = (x, y)
            if pos not in visited:
                visited.append(pos)
                houses += 1

        return houses

    @staticmethod
    def solve_one(path=day_three):
        """
        This isn't really even a better solution, it's just more stupid.
        """
        houses = 1
        x = y = 0
        visited = [(0, 0)]

        switch = {
            '^': lambda x, y: (x, y+1),
            '>': lambda x, y: (x+1, y),
            'v': lambda x, y: (x, y-1),
            '<': lambda x, y: (x-1, y),
        }

        for move in path:
            x, y = switch[move](x, y)
            if (x, y) not in visited:
                visited.append((x, y))
                houses += 1

        return houses

    @staticmethod
    def solve_two(path=day_three):
        x = y = 0
        visited = {(x, y)}

        switch = {
            '^': lambda x, y: (x, y+1),
            '>': lambda x, y: (x+1, y),
            'v': lambda x, y: (x, y-1),
            '<': lambda x, y: (x-1, y),
        }

        for move in path:
            x, y = switch[move](x, y)
            visited.add((x, y))

        return len(visited)

    @staticmethod
    def solve_three(path=day_three):
        """h/t to /u/ratmatrix for the dict lambda"""
        santa = (0, 0)
        visited = {santa}

        for move in path:
            santa = (lambda x, y, d: {'^': (x, y+1), '>': (x+1, y), 'v': (x, y-1), '<': (x-1, y)}[d])(*santa, move)
            visited.add(santa)

        return len(visited)


class PartTwo:
    """
    --- Part Two ---

    The next year, to speed up the process, Santa creates a robot version of
    himself, Robo-Santa, to deliver presents with him.

    Santa and Robo-Santa start at the same location (delivering two presents to
    the same starting house), then take turns moving based on instructions from
    the elf, who is eggnoggedly reading from the same script as the previous year.

    This year, how many houses receive at least one present?

    For example:

      - ^v delivers presents to 3 houses, because Santa goes north, and then
      Robo-Santa goes south.
      - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end
      up back where they started.
      - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one
      direction and Robo-Santa going the other.

    Solution: 2639
    """
    @staticmethod
    def solve(path=day_three):

        santa, robot = (0, 0), (0, 0)
        visited = {santa}
        switch = {
            '^': lambda x, y: (x, y+1),
            '>': lambda x, y: (x+1, y),
            'v': lambda x, y: (x, y-1),
            '<': lambda x, y: (x-1, y),
        }

        for i in range(len(path)):
            if i % 2:
                robot = switch[path[i]](*robot)
                visited.add(robot)
            else:
                santa = switch[path[i]](*santa)
                visited.add(santa)

        return len(visited)

    @staticmethod
    def solve_one(path=day_three):
        movers = [(0, 0), (0, 0)]
        visited = {movers[0]}
        switch = {
            '^': lambda x, y: (x, y+1),
            '>': lambda x, y: (x+1, y),
            'v': lambda x, y: (x, y-1),
            '<': lambda x, y: (x-1, y),
        }

        for i in range(len(path)):
            movers[i % 2] = switch[path[i]](*movers[i % 2])
            visited.add(movers[i % 2])

        return len(visited)
