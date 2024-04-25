#!/usr/bin/python3
"""funcion that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """
Seeking a peak value within an unsorted list of integers is the task at hand. Our aim is to devise an algorithm with the utmost efficiency. It's worth noting that multiple peaks may exist within the list.

A straightforward approach involves iterating through each element individually, assessing its candidacy as a peak. This method typically requires O(n) time complexity at its worst, with space complexity remaining constant at O(1), which suffices for most algorithmic problems. However, our challenge lies in achieving a time complexity of O(log(n)).

While Binary Search is commonly employed in sorted arrays, adapting it to an unsorted array presents a unique challenge. In Binary Search, the middle value is evaluated for its peak potential, and subsequent adjustments to the start or end pointers are made accordingly to obtain a new middle value.

Function Parameters:
- list_of_integers (list): A list containing integers.

Returns:
    int: The peak(s) identified.
"""

    list_ = list_of_integers
    
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
