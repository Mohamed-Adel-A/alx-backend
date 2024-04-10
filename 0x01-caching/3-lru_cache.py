#!/usr/bin/env python3
"""Defines LRUCache class"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Defines a caching system with LRU eviction policy"""

    def __init__(self):
        """Initializes the LRUCache instance"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]
