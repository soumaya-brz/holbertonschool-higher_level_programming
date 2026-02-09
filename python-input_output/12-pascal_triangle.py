#!/usr/bin/python3
"""Module that returns Pascal's triangle."""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # première ligne

    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]  # premier élément
        # éléments intermédiaires
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # dernier élément
        triangle.append(new_row)

    return triangle
