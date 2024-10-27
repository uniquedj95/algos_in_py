
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