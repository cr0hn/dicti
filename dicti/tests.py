#!/usr/bin/env python2
# -*- encoding: utf-8 -*-
from unittest import TestCase, main
from dicti import dicti

class TestInit(TestCase):
    def test__init__(self):
        """Create an empty dictionary, or update from 'dict'."""
        d = {3: "u", "oeuoaue": []}
        di = dicti(d)
        self.assertEqual(d[3], di._dict[3][1])

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
        v_di = self.di.values()
        v_d = self.d.values()

        v_di.sort()
        v_d.sort()

        self.assertListEqual(v_d, v_di)

class TestItems(TestDicti):
    def test_items(self):
        self.assertDictEqual(dict(self.di.items()), dict(self.d.items()))

class TestGet(TestDicti):
    def test_get_default(self):
        self.assertEquals(self.di.get(None, 42), 42)

    def test_get(self):
        for k, v in self.d.items():
            keys = [k]
            try:
                keys.extend([k.lower(), k.upper()])
            except AttributeError:
                pass

            for key in keys:
                self.assertEqual(self.di.get(key), v)

#class TestSetDefault(TestDicti):
#    def test_setdefault(self):

class TestUpdate(TestDicti):
    def test_update(self):
        new = {'mnoeOENUTH': 'h'}
        self.d.update(new)
        self.di.update(new)
        self.assertEqual(self.d.items(), self.di.items())

class TestStringRepresentation(TestDicti):
    def test_represent(self):
        self.assertEqual(str(self.di), str(self.d))
        self.assertEqual(repr(self.di), repr(self.d))
        self.assertEqual(unicode(self.di), unicode(self.d))

class TestCompleteness(TestCase):
    def test_dir(self):
        self.assertListEqual(dir(dict), dir(dicti))

if __name__ == '__main__':
    main()
