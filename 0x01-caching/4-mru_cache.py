#!/usr/bin/env python3
"""Defines MRUCache class"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Defines a caching system with MRU eviction policy"""

    def __init__(self):
        """Initializes the MRUCache instance"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = max(self.cache_data, key=self.cache_data.get)
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
