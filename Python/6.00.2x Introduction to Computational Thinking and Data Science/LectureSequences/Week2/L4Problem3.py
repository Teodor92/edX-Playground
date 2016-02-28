import math

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    if len(L) == 0:
        return float('nan')

    stringLengths = []
    deviation = 0

    for string in L:
        stringLengths.append(len(string))

    mean = float(sum(stringLengths)) / len(stringLengths) if len(stringLengths) > 0 else float('nan')

    for length in stringLengths:
        deviation += (length - mean) * (length - mean)

    return math.sqrt(deviation / len(stringLengths))