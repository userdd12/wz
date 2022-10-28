"""
Project Euler Problem 61: https://projecteuler.net/problem=61

Problem Statement:

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are
all figurate (polygonal) numbers and are generated by the following formulae:
    Triangle   ->  P3,n=n(n+1)/2   ->  1, 3, 6, 10, 15, ...
    Square     ->  P4,n=n2         ->  1, 4, 9, 16, 25, ...
    Pentagonal ->  P5,n=n(3n-1)/2  ->  1, 5, 12, 22, 35, ...
    Hexagonal  ->  P6,n=n(2n-1)    ->  1, 6, 15, 28, 45, ...
    Heptagonal ->  P7,n=n(5n-3)/2  ->  1, 7, 18, 34, 55, ...
    Octagonal  ->  P8,n=n(3n-2)    ->  1, 8, 21, 40, 65, ...

The ordered set of three 4-digit numbers: 8128, 2882, 8281,
 has three interesting properties.

1. The set is cyclic, in that the last two digits of each
    number is the first two digits of the next number
    (including the last number with the first).
2. Each polygonal type: triangle (P3,127=8128), square
    (P4,91=8281), and pentagonal (P5,44=2882), is
    represented by a different number in the set.
3. This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic
4-digit numbers for which each polygonal type:
    triangle, square, pentagonal, hexagonal, heptagonal, and
    octagonal, is represented by a different number in the set.
"""

# Global variables (permanent sets)
megaset = set()
set3 = set()
set4 = set()
set5 = set()
set6 = set()
set7 = set()
set8 = set()


# Functions to check for every family of numbers in the question
def if_octagonal_number(number: int) -> bool:
    """
    Returns a bool to tell whether the number is an octagonal number.

    >>> if_octagonal_number(8)
    True
    >>> if_octagonal_number(20)
    False
    """

    if ((1 + (1 + 3 * number) ** (1 / 2)) / 3) % 1 == 0:
        return True
    else:
        return False


def if_heptagonal_number(number: int) -> bool:
    """
    Returns a bool to tell whether the number is an heptagonal number.

    >>> if_heptagonal_number(7)
    True
    >>> if_heptagonal_number(91)
    False
    """

    if ((3 + (9 + 40 * number) ** (1 / 2)) / 10) % 1 == 0:
        return True
    else:
        return False


def if_hexagonal_number(number: int) -> bool:
    """
    Returns a bool to tell whether the number is an hexagonal number.

    >>> if_hexagonal_number(15)
    True
    >>> if_hexagonal_number(20)
    False
    """

    temp = (1 + (8 * number + 1) ** (1 / 2)) / 4
    if temp % 1 == 0:
        return True
    else:
        return False


def if_pentagonal_number(number: int) -> bool:
    """
    Returns a bool to tell whether the number is an pentagonal number.

    >>> if_pentagonal_number(12)
    True
    >>> if_pentagonal_number(30)
    False
    """

    temp = (1 + (24 * number + 1) ** (1 / 2)) / 6
    if temp % 1 == 0:
        return True
    else:
        return False


def if_triangle_number(number: int) -> bool:
    """
    Returns a bool to tell whether the number is an triangle number.

    >>> if_triangle_number(10)
    True
    >>> if_triangle_number(39)
    False
    """

    temp = (-1 + (1 + 8 * number) ** (1 / 2)) / 2
    if temp % 1 == 0:
        return True
    else:
        return False


def check_cycle_condition(answers: list) -> bool:
    """
    Checks whether the cycle has one of every type of number

    >>> check_cycle_condition([1,2,3,4,5,6])
    True

    >>> check_cycle_condition([2,4,5,3,2,3])
    False
    """

    check_list = []
    for ele in answers:
        if ele in set3:
            check_list.append(3)
        if ele in set4:
            check_list.append(4)
        if ele in set5:
            check_list.append(5)
        if ele in set6:
            check_list.append(6)
        if ele in set7:
            check_list.append(7)
        if ele in set8:
            check_list.append(8)
    if len(set(check_list)) == 6:
        return True
    else:
        return False


def solution() -> int:
    """
    Checks for all the 4 digit numbers.
    Returns the sum of the set of numbers that has one of each kind of number.

    >>> solution()
    28684
    """
    # Makes megaset and separate sets from all 4 digit numbers
    for number in range(1000, 10000):
        if if_triangle_number(number) and str(number)[2:3] != "0":
            megaset.add(number)
            set3.add(number)
        if (number ** (1 / 2)) % 1 == 0 and str(number)[2:3] != "0":
            megaset.add(number)
            set4.add(number)
        if if_pentagonal_number(number) and str(number)[2:3] != "0":
            megaset.add(number)
            set5.add(number)
        if if_hexagonal_number(number) and str(number)[2:3] != "0":
            megaset.add(number)
            set6.add(number)
        if if_heptagonal_number(number) and str(number)[2:3] != "0":
            megaset.add(number)
            set7.add(number)
        if if_octagonal_number(number) and str(number)[2:3] != "0":
            megaset.add(number)
            set8.add(number)

    # Tries all combinations of sets and megasets and checks
    # for condition mentioned in question
    # Only tests for numbers that don't repeat
    #   (none of the n_ are same in value, where '_' is any number)
    for n1 in set8:
        for n2 in megaset:
            if str(n2)[:2] == str(n1)[-2:] and n2 != n1:
                for n3 in megaset:
                    if str(n3)[:2] == str(n2)[-2:] and n3 != n2 and n3 != n1:
                        for n4 in megaset:
                            if (
                                str(n4)[:2] == str(n3)[-2:]
                                and n4 != n3
                                and n4 != n2
                                and n4 != n1
                            ):
                                for n5 in megaset:
                                    if (
                                        str(n5)[:2] == str(n4)[-2:]
                                        and n5 != n4
                                        and n5 != n3
                                        and n5 != n2
                                        and n5 != n1
                                    ):
                                        for n6 in megaset:
                                            if (
                                                str(n6)[:2] == str(n5)[-2:]
                                                and n6 != n5
                                                and n6 != n4
                                                and n6 != n3
                                                and n6 != n2
                                                and n6 != n1
                                                and str(n1)[:2] == str(n6)[-2:]
                                            ):
                                                loc = [n1, n2, n3, n4, n5, n6]
                                                if check_cycle_condition(loc):
                                                    return sum(loc)
    return 0


if __name__ == "__main__":
    print(solution())
