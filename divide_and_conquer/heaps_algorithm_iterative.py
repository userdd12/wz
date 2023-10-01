"""
Heap's (iterative) algorithm returns the list of all permutations possible from a list.
It minimizes movement by generating each permutation from the previous one
by swapping only two elements.
More information:
https://en.wikipedia.org/wiki/Heap%27s_algorithm.
"""

def heaps(arr: list) -> list:
    """
    Pure python implementation of the Heap's algorithm (recursive version),
    returning all permutations of a list.

    >>> heaps([])
    [()]
    >>> heaps([0])
    [(0,)]
    >>> heaps([-1, 1])
    [(-1, 1), (1, -1)]
    >>> heaps([1, 2, 3])
    [(1, 2, 3), (2, 1, 3), (3, 1, 2), (1, 3, 2), (2, 3, 1), (3, 2, 1)]
    """

    def generate(k: int, arr: list, res: list):
        if k == 1:
            res.append(tuple(arr))
            return

        generate(k - 1, arr, res)

        for i in range(k - 1):
            if k % 2 == 0:  # k is even
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
            else:  # k is odd
                arr[0], arr[k - 1] = arr[k - 1], arr[0]
            generate(k - 1, arr, res)

    if len(arr) <= 1:
        return [tuple(arr)]

    res = []
    generate(len(arr), arr, res)
    return res


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    print(heaps(arr))
