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
        self.mru_key = None

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            if self.mru_key:
                del self.cache_data[self.mru_key]
                print("DISCARD:", self.mru_key)

        self.cache_data[key] = item
        self.mru_key = key

    def get(self, key):
        """
        Gets an item from the cache by key and if key doesn't exist or is
        None, returns None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
