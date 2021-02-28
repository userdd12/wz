def isGeometricMean(series: list) -> bool:
    """
    checking whether the input series is geometric series or not

    >>> isGeometricMean([2, 4, 8])
    True
    >>> isGeometricMean([3, 6, 12, 24])
    True
    >>> isGeometricMean([1, 2, 3])
    False

    """
    if len(series) == 1:
        return True
    common_ratio = series[1] / series[0]
    for index in range(len(series) - 1):
        if series[index + 1] / series[index] != common_ratio:
            return False
    return True


def geometric_mean(series: list) -> float:
    """
    return the geometric mean of series

    >>> geometric_mean([2, 4, 8])
    3.9999999999999996
    >>> geometric_mean([3, 6, 12, 24])
    8.48528137423857
    >>> geometric_mean([4, 8, 16])
    7.999999999999999
    >>> geometric_mean([1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: Input list is not a geometric series
    >>> geometric_mean([])
    Traceback (most recent call last):
        ...
    ValueError: Input list must be a non empty list

    """
    if len(series) == 0:
        raise ValueError("Input list must be a non empty list")
    if not isGeometricMean(series):
        raise ValueError("Input list is not a geometric series")
    answer = 1
    for _ in series:
        answer *= _
    return pow(answer, 1 / len(series))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
