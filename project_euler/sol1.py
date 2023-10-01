"""
Problem 95
Url: https://projecteuler.net/problem=95
Statement:
The proper divisors of a number are all the divisors excluding the number itself.
For example, the proper divisors of  28 is 1,2,4,7 and 14 and .
As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220 forming a chain of two numbers.
For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
12496 -> 14288 -> 15472 -> 14536 -> 14264(->12496 -> ....)
Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""


def find_smallest_member(n: int) -> int:
    """
    Returns the smallest member of the longest amicable chain with no element exceeding one million
    >> 14316
    """

    sum_of_div = [0] * (n + 1)
    for i in range(1, n // 2 + 1):
        for j in range(i * 2, n + 1, i):
            sum_of_div[j] += i

    checked = [False] * (n + 1)
    max_chain_len = 0
    result = 0
    for i in range(2, n + 1):
        possible_chain = []
        j = i
        while not checked[j]:
            checked[j] = True
            possible_chain.append(j)
            j = sum_of_div[j]
            if j > n:
                break
            if j in possible_chain:
                len_of_chain = len(possible_chain) - possible_chain.index(j)
                if len_of_chain > max_len_of_chain:
                    max_len_of_chain = len_of_chain
                    result = min(possible_chain[-len_of_chain:])
                break
    return result


if __name__ == "__main__":
    print(f"Solution : {find_smallest_member(10**6)}")
