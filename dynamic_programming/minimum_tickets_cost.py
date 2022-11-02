"""
Author  : Alexander Pantyukhin
Date    : November 1, 2022

Task:
Given a list of days when you need to travel. Each day is integer from 1 to 365.
You are able to use tickets for 1 day, 7 days and 30 days.
Each ticket has a cost.

Find the minimum cost you need to travel every day in the given list of days.

Implementation notes:
implementation Dynamic Programming up bottom approach.

Runtime complexity: O(n)

The implementation was tested on the
leetcode: https://leetcode.com/problems/minimum-cost-for-tickets/
Minimum Cost For Tickets
Dynamic Programming: up -> down.
"""


def mincost_tickets(days: List[int], costs: List[int]) -> int:
    """
    >>> mincost_tickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
    11

    >>> mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],  [2, 7, 15])
    17

    >>> mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    24

    >>> mincost_tickets([2], [2, 90, 150])
    2

    >>> mincost_tickets([], [2, 90, 150])
    0

    >>> mincost_tickets('hello', [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: The parameter days should be a list

    >>> mincost_tickets([], 'world')
    Traceback (most recent call last):
     ...
    ValueError: The parameter costs should be a list

    >>> mincost_tickets([0.25, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: All days elements should be integer values

    >>> mincost_tickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 0.9, 150])
    Traceback (most recent call last):
     ...
    ValueError: All costs elements should be integer values

    >>> mincost_tickets([-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: All days elements should be greater than 0

    >>> mincost_tickets([2, 367], [2, 90, 150])
    Traceback (most recent call last):
     ...
    ValueError: All days elements should be less than 366

    >>> mincost_tickets([2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [])
    Traceback (most recent call last):
     ...
    ValueError: The lengths of costs should be equal 3

    >>> mincost_tickets([], [])
    Traceback (most recent call last):
     ...
    ValueError: The lengths of costs should be equal 3

    >>> mincost_tickets([2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [1, 2, 3, 4])
    Traceback (most recent call last):
     ...
    ValueError: The lengths of costs should be equal 3
    """

    # Validation
    if not isinstance(days, list):
        raise ValueError("The parameter days should be a list")

    if not isinstance(costs, list):
        raise ValueError("The parameter costs should be a list")

    if any([not isinstance(day, int) for day in days]):
        raise ValueError("All days elements should be integer values")

    if any([not isinstance(cost, int) for cost in costs]):
        raise ValueError("All costs elements should be integer values")

    if len(costs) != 3:
        raise ValueError("The lengths of costs should be equal 3")

    if len(days) == 0:
        return 0

    if min(days) <= 0:
        raise ValueError("All days elements should be greater than 0")

    if max(days) >= 366:
        raise ValueError("All days elements should be less than 366")

    from functools import lru_cache

    days_set = set(days)

    @lru_cache(maxsize=None)
    def dp(index: int) -> int:
        """
        >>> dp(366)
        0
        """

        if index > 365:
            return 0

        if index not in days_set:
            return dp(index + 1)

        return min(
            costs[0] + dp(index + 1), 
            costs[1] + dp(index + 7), 
            costs[2] + dp(index + 30), 
        )

    return dp(1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
