#!/usr/bin/env python3
"""
This module defines a function returns a size two tuple containing a start
and end indices corresponding to the indices range to return in a list
of certain pagination parameters
"""


def index_range(page: int, page_size: int) -> Tuple:
    """
    Function takes two params, calculates start and end index
    for a page and page size
    page: page of interest
    page_size: number of items in a page
    return: size two tuple
    """
    # current page items start
    start = (page - 1) * page_size

    # current page items end in the list
    end = start + page_size
    return (start, end)
