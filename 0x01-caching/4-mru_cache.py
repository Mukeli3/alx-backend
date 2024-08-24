#!/usr/bin/python3
"""
MRUCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache is a caching system that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize the class and call the parent init method.
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item

            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    mru_key = next(reversed(self.cache_data))
                    self.cache_data.pop(mru_key)
                    print("DISCARD:", mru_key)

            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache by key and if key doesn't exist or is
        None, returns None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
