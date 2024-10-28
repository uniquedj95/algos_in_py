
from typing import List


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

def countingSort(arr):
    """
    Count the number of times each value appears in a given array of integers

    :param arr: List[int] - an array of integers
    :return: List[int] - a frequency array of size 100
    """
    return [sum(1 for x in arr if x == i) for i in range(100)]

def pangram(s):
    """
    Determine if a given string is a Pangram or Not. A Pangram is a string that contains every letter of the alphabet.

    :param s: str - A string to be checked
    :return: str - pangram OR not pangram
    """
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return "pangram" if alphabet <= set(s.lower()) else "not pangram"

def permuteArray(k: int, A: List[int], B: List[int]) -> str:
    """
    Permute arrays A and B into A' and B' such that A'[i] + B'[i] >= k

    :param k: int - an integer between 0 and 10^9
    :param A: List[int] - an array of integers of n size
    :param B: List[int] - an array of integers of n size
    :return: str - YES if the relation exists. NO otherwise
    """
    return "YES" if all(a + b >= k for a, b in zip(sorted(A), sorted(B, reverse=True))) else "NO"

def subArrayDivision(s: List[int], d: int, m: int) -> int:
    """
    Calculate the number of ways to divide an array into contigous sub arrays of length m which sums to d

    :param s: List[int] - an array of integers
    :param d: int - an integer representing the sum of the sub arrays
    :param m: int - an integer representing the length of the sub arrays
    :return: int - the number of ways the given array can be divided
    """
    return sum(1 for i in range(len(s) - m + 1) if sum(s[i:i + m]) == d)

def longestSubString(s: str) -> int:
    """
    Find the length of the longest substring of a given string without repeating characters

    :param s: str - a string of length n
    :return: int - the length of the longest substring
    """
    longest = 0
    start = 0
    seen = {}
    for i, char in enumerate(s):
        if char in seen:
            start = max(start, seen[char] + 1)
        seen[char] = i
        longest = max(longest, i - start + 1)
    return longest