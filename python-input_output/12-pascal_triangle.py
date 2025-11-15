#!/usr/bin/python3
"""Generate Pascal's Triangle up to a given number of rows"""


def pascal_triangle(n):
    """Generates Pascal's Triangle up to n."""
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)
        triangle.append(row)
    return (triangle)
