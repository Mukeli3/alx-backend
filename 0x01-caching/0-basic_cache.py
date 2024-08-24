#!/usr/bin/python3
"""
This module defines a class that's a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    caching system that inherits from BaseCaching and
    doesn't have a limit
    """
    def put(self, key, item):
        """
        Add an item to the cache and does nothing if key or item
        is None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache by key and if key doesn't exist or is
        None, returns None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
