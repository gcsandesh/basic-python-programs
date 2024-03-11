def kangaroo(x1, v1, x2, v2):
    """
    params:
    x1 = start position of kangaroo 1
    v1 = jump velocity of kangaroo 1
    x2 = start position of kangaroo 2
    v2 = jump velocity of kangaroo 2

    return: string("YES"/"NO")

    The kangaroo function will find if both kangaroos meet a point.

    """
    # first eliminating all obvious conditions
    if x2 == x1:  # if they already meet at 0 jumps
        return "YES"
    elif (
        x1 > x2 and v1 > v2
    ):  # if first is ahead and is faster than second, they'll never meet
        return "NO"
    elif (
        x2 > x1 and v2 > v1
    ):  # if second is ahead and is faster than first, they'll never meet
        return "NO"
    elif (v1 - v2) == 0:  # if relative velocity is 0
        if x1 == x2:  # if they are at same position, they will meet
            return "YES"
        else:  # if any one is ahead of another, they will not meet
            return "NO"

    """
    for both to meet at a point,
    x1 + n*v1 = x2 + n*v2,
    i.e. at finite number of jumps(n),
    their position should be equal.
    i.e. n must be a positive integer
    """

    if (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) / (v1 - v2) > 0:
        return "YES"
    return "NO"
