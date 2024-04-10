#!/usr/bin/env python3
"""Defines FIFOCache class"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """Defines a caching system with FIFO eviction policy"""

    def __init__(self):
        """Initializes the FIFOCache instance"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded = self.queue.pop(0)
            del self.cache_data[discarded]
            print("DISCARD:", discarded)
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
