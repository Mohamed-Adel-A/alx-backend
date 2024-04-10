#!/usr/bin/env python3
"""Defines BasicCache class"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Defines a basic caching system"""

    def __init__(self):
        """Initializes the BasicCache instance"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
