#!/usr/bin/env python3
"""
Hypermedia pagination
"""

from typing import List, Dict
from 0-simple_pagination import Server


class Server(Server):
    """Enhanced Server class with hypermedia pagination."""
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return hypermedia pagination information."""
        data = self.get_page(page, page_size)
        total_pages = len(self.dataset()) // page_size + 1
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
