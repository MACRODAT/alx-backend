#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    tmp = page * page_size
    return max(0, tmp - page_size), tmp
