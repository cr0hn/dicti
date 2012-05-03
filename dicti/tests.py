#!/usr/bin/env python2
# -*- encoding: utf-8 -*-

# This file is part of dicti.

# dicti is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# dicti is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.

# You should have received a copy of the GNU Affero Public License
# along with dicti.  If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase, main
from dicti import dicti
import random

class TestInit(TestCase):
    def test__init__(self):
        """Create an empty dictionary, or update from 'dict'."""
        d = {3: "u", "oeuoaue": []}
        di = dicti(d)
        self.assertEqual(d[3], di[3])

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

class TestRewrite(TestCase):
    def test_rewrite(self):
        di = dicti()
        di['cAsE'] = 1
        self.assertEqual(di['case'], 1)
        di['Case'] = 2
        self.assertEqual(di['case'], 2)

        self.assertListEqual(di.keys(), ['Case'])
        self.assertListEqual(di.values(), [2])

class TestReadmeExamples(TestCase):
    def test_init(self):
        d = dict(foo = 'bar', answer = 42)
        di = dicti(foo = 'bar', answer = 42)
        self.assertEqual(d.items(), di.items())
        
        d = dict({'foo': 'bar', 'answer': 42})
        di = dicti({'foo': 'bar', 'answer': 42})
        self.assertEqual(d.items(), di.items())

        di = dicti()
        di['cAsE'] = 1
        self.assertListEqual(di.keys(), ['cAsE'])
        di['Case'] = 1
        self.assertListEqual(di.keys(), ['Case'])
        self.assertEqual(di['caSE'], 1)

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

class TestIter(TestDicti):
    def test_iter(self):
        k_observed = [k for k in self.di]
        k_expected = [k for k in self.d]
        self.assertEqual(k_observed, k_expected)

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

class TestPop(TestDicti):
    def test_pop_default(self):
        self.assertEquals(self.di.pop(None, 42), 42)

class TestReSetItem(TestDicti):
#   def test_reset_many(self):
#       for k, v in self.d.items():
#           keys = [k]
#           try:
#               keys.extend([k.lower(), k.upper()])
#           except AttributeError:
#               pass

#           for key in keys:
#               self.di[key] = v
#               self.assertEqual(self.di.pop(key), v)
#               self.assertRaises(KeyError, lambda: self.di.pop(key))

    def test_reset(self):
        di = dicti()
        di['oeuOEU'] = 3
        del(di['oeuoeu'])
        di['oEuOeU'] = 3
        di['oEuOEU'] = 3
        del(di['oeuoeu'])

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

#class TestCompleteness(TestCase):
#    def test_dir(self):
#        self.assertListEqual(dir(dict), dir(dicti))

if __name__ == '__main__':
    main()
