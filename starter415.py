# Recitation Activity #10

def hailstone(num):
    '''
        >>> itr1 = hailstone(3)
        >>> next(itr1)
        3
        >>> next(itr1)
        10
        >>> next(itr1)
        5
        >>> next(itr1)
        16
        >>> next(itr1)
        8
        >>> next(itr1)
        4
        >>> next(itr1)
        2
        >>> next(itr1)
        1
        >>> next(itr1)
        Traceback (most recent call last):
        ...
        StopIteration
        >>> itr2 = hailstone(6)
        >>> [item for item in itr2]
        [6, 3, 10, 5, 16, 8, 4, 2, 1]
    '''
    yield num
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        yield int(num)
