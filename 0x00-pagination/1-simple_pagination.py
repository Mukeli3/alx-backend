#!/usr/bin/env python3
"""
This module defines a class that aids in pagination of a database
of popular baby names
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        retrieve data page from the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
