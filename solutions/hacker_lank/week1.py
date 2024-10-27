
def minusPlus(arr):
    """
    Calculates and prints the fractions of positive, negative, and zero elements in the given array.

    param: arr: List[int] - The input list of integers.
    return: None: This function prints the fractions of positive, negative, and zero elements in the array.
    """
    total = len(arr)
    pos_count = sum(1 for x in arr if x > 0)
    neg_count = sum(1 for x in arr if x < 0)
    zero_count = total - pos_count - neg_count
    
    print(f"{pos_count / total:.6f}")
    print(f"{neg_count / total:.6f}")
    print(f"{zero_count / total:.6f}")


def matchingStrings(strings, queries):
    """
    Count the number of occurrences of each query in the strings

    :param strings: List[str] - list of strings
    :param queries: List[str] - list of queries
    :return: List[int] - list of counts of each query
    """
    return [sum(1 for string in strings if string == query) for query in queries]

def lonelyinteger(a):
    """
    Find the integer that appears only once in the list

    :param a: List[int] - list of integers
    :return: int - integer that appears only once
    """
    return 2 * sum(set(a)) - sum(a)

def timeConversion(s):
    """
    Convert time from 12-hour format to 24-hour format

    :param s: str - time in 12-hour format
    :return: str - time in 24-hour format
    """
    hh, mm, ss = map(int, s[:-2].split(":"))
    period = s[-2:]

    if period == "AM":
        hh = hh % 12
    else:
        hh = (hh % 12) + 12

    return f"{hh:02d}:{mm:02d}:{ss:02d}"

def flippingBits(n):
    """
    This function takes a 32-bit unsigned integer and flips all the bits (i.e., changes 1s to 0s and 0s to 1s).

    :param n: int - a long integer to be flipped
    :return: int - the flipped long integer

    Example:
    >>> flippingBits(1)
    4294967294
    >>> flippingBits(4294967294)
    1

    Explanation:
    Unsigned 32-bits of 1 is 00000000000000000000000000000001. when flipped is 11111111111111111111111111111110
    which is 4294967294
    """
    return n ^ 0xFFFFFFFF


def absoluteDifference(arr):
    """
    Calculate the absolute difference between the sums of a given matrix diagonals.

    :param arr: List[int] - an N x M array of integers / an N x M matrix
    :return: int - the absolute diagonal difference 
    """
    primary_diagonal = sum(arr[i][i] for i in range(len(arr)))
    secondary_diagonal = sum(arr[i][len(arr) - 1 - i] for i in range(len(arr)))
    return abs(primary_diagonal - secondary_diagonal)