#!/usr/bin/python3
"""
This module defines LRUCache caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache caching system
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.cache_data = {}
        self.order = []

    def put(self, key, item):
        """
        Add item
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.order.remove(key) # remove old posn
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lru_key = self.order.pop(0)
                    self.cache_data.pop(lru_key)
                    print("DISCARD:", lru_key)

            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache by key and if key doesn't exist or is
        None, returns None
        """
        if key is None:
            return None
        return self.cache_data.get(key)
