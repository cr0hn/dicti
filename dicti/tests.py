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

class TestKeys(TestDicti):
    def test_keys(self):
        self.assertSetEqual(set(self.di.keys()), set(self.d.keys()))

class TestValues(TestDicti):
    def test_values(self):
        self.assertSetEqual(set(self.di.values()), set(self.d.values()))

class TestItems(TestDicti):
    def test_items(self):
        self.assertDictEqual(dict(self.di.items()), dict(self.d.items()))

class TestGet(TestDicti):
    def test_get_default(self):
        self.assertEquals(self.di.get(42), 42)

    def test_get(self):
        for k, v in self.d.keys():
            keys = [k]
            try:
                keys.extend([k.lower(), k.upper()])
            except AttributeError:
                pass

            for key in keys:
                self.assertEqual(self.di.get(key), v)

class TestSetDefault(TestDicti):
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
