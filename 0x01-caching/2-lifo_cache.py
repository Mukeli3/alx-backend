#!/usr/bin/python3
"""
This module defines a class LIFOCache which is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import OrderedDict

class LIFOCache(BaseCaching):
    """
    LIFOCache is a caching system that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize the class and call the parent init method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache and does nothing if key or item
        is None
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Gets an item from the cache by key and if key doesn't exist or is
        None, returns None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
