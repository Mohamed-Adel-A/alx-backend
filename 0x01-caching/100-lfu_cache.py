#!/usr/bin/env python3
"""Defines LFUCache class"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Defines a caching system with LFU eviction policy"""

    def __init__(self):
        """Initializes the LFUCache instance"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                least_frequent = [k for k, v in self.frequency.items() if v == min_freq]
                if len(least_frequent) > 1:
                    lru_key = min(self.cache_data, key=self.cache_data.get)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    del self.cache_data[least_frequent[0]]
                    del self.frequency[least_frequent[0]]
                    print("DISCARD:", least_frequent[0])
            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        return self.cache_data[key]
