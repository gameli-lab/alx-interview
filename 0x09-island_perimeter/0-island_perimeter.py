#!/usr/bin/python3
''' island module'''


def island_perimeter(grid):
    ''' island method'''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                '''
                Check the four sides
                Up
                '''
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                ''' Down'''
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                ''' Left'''
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                ''' Right'''
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
