#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict
from 0-simple_helper_function import index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(dataset)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return hypermedia pagination information based on index."""
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0
        
        dataset = self.indexed_dataset()
        max_index = len(dataset) - 1
        
        if index is not None:
            start_index = index
        else:
            start_index = 0
        
        end_index = min(start_index + page_size, max_index + 1)
        
        data = [dataset[i] for i in range(start_index, end_index)]
        
        next_index = end_index if end_index < max_index else None
        
        return {
            'index': start_index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
