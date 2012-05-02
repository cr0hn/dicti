#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from unittest import TestCase, main
from dicti import dicti

class TestInit(TestCase):
    def test__init__(self):
        """Create an empty dictionary, or update from 'dict'."""
        d = {3: "u", "oeuoaue": []}
        di = dicti(d)
        self.assertDictEqual(d, di._dict)

class TestDicti(TestCase):
    def setUp(self):
        self.d = {
            '詞典': 'foo',
            3: 'uaoeua',
            'uOUoeu': [],
            'Th': {'oM': 'as'},
        }
        self.di = dicti(self.d)

class TestGetItem(TestDicti):
    def test__getitem__(self):
        for k, v in self.d.items():
            keys = [k]
            try:
                keys.extend([k.lower(), k.upper()])
            except AttributeError:
                pass

            for key in keys:
                self.assertEqual(self.di[k], v)
import random

class TestSetItem(TestDicti):
    def test__setitem__(self):
        for k in self.d.keys():
            keys = [k]
            try:
                keys.extend([k.lower(), k.upper()])
            except AttributeError:
                pass

            for key in keys:
                v = random.random()
                self.di[key] = v
                self.assertEqual(self.di[key], v)

class TestHasKey(TestDicti):
    def test_has_key(self):
        for k in self.d.keys():
            keys = [k]
            try:
                keys.extend([k.lower(), k.upper()])
            except AttributeError:
                pass

            for key in keys:
                self.assertTrue(self.di.has_key(key))

    def keys(self):
        """List of keys in their original case."""
        return [v[0] for v in self._dict.values()]

    def values(self):
        """List of values."""
        return [v[1] for v in self._dict.values()]

    def items(self):
        """List of (key,value) pairs."""
        return self._dict.values()

    def get(self, key, default=None):
        """Retrieve value associated with 'key' or return default value
        if 'key' doesn't exist."""
        try:
            return self[key]
        except KeyError:
            return default

    def setdefault(self, key, default):
        """If 'key' doesn't exists, associate it with the 'default' value.
        Return value associated with 'key'."""
        if not self.has_key(key):
            self[key] = default
        return self[key]

    def update(self, dict):
        """Copy (key,value) pairs from 'dict'."""
        for k,v in dict.items():
            self[k] = v

    def __repr__(self):
        """String representation of the dictionary."""
        items = ", ".join([("%r: %r" % (k,v)) for k,v in self.items()])
        return "{%s}" % items

    def __str__(self):

if __name__ == '__main__':
  main()
