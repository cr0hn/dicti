#!/usr/bin/env python2
from unittest import TestCase, main
from dicti import dicti

class TestInit(TestCase):
    def compare(self, method, *args, **kwargs):
        'Run something on both dictionaries'
        method(*args, **kwargs)

if __name__ == '__main__':
  main()
