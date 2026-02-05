#!/usr/bin/env python3


class CountedIterator:
    """Iterator that counts how many items have been iterated over."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        return self

    def get_count(self):
        return self.count
