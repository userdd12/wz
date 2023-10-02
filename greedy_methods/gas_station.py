"""
Task:
There are n gas stations along a circular route, where the amount of gas
at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas
to travel from the ith station to its next (i + 1)th station. You begin the
journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique

Reference: https://leetcode.com/problems/gas-station/description

Implementation notes:
First, check whether the total gas is enough to complete the journey. If not, return -1.
However, if there is enough gas, it is guaranteed that there is a valid
starting index to reach the end of the journey.
Greedily calculate the net gain (gas - cost) at each station.
If the net gain ever goes below 0 while iterating through the stations,
start checking from the next station.

"""


def can_complete_journey(gas: list[int], cost: list[int]) -> int:
    """
    This function returns the index from which to start the journey
    in order to reach the end.

    Args:
        gas [list]: Amount of gas available at each station
        cost [list]: The cost of gas required to move from a station to the next

    Returns:
        start [int]: start index needed to complete the journey

    Examples:
    >>> can_complete_journey([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    3
    >>> can_complete_journey([2, 3, 4], [3, 4, 3])
    -1

    """
    total_gas = sum(gas)
    total_cost = sum(cost)

    if total_gas < total_cost:
        return -1

    start = 0
    net = 0
    for i in range(len(gas)):
        net += gas[i] - cost[i]
        if net < 0:
            start = i + 1
            net = 0

    return start


if __name__ == "__main__":
    import doctest

    doctest.testmod()
