#!/usr/bin/python3
"""
This module defines a class that inherits from BaseCaching and
is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache is a caching system that inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.korder = []

    def put(self, key, item):
        """
        Add an item to the cache and does nothing if key or item
        is None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        self.korder.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            fkey = self.korder.pop(0)
            del self.cache_data[fkey]
            print(f"DISCARD: {fkey}")

    def get(self, key):
        """
        Gets an item from the cache by key and if key doesn't exist or is
        None, returns None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
