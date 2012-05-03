#!/usr/bin/env python2

# By Sami, packaged by Tom
# http://code.activestate.com/recipes/66315-case-insensitive-dictionary/

def lower(potentialstring):
    'Lowercase the potential string if possible'
    try:
        return potentialstring.lower()
    except AttributeError:
        return potentialstring

class dicti:
    """Dictionary with case-insensitive keys.
    
    Keys are retained in their original form
    when queried with .keys() or .items().

    Implementation: An internal dictionary maps lowercase
    keys to (key,value) pairs. All key lookups are done
    against the lowercase keys, but all methods that expose
    keys to the user retrieve the original keys."""

    def __init__(self, *args, **kwargs):
        """Create an empty dictionary, or update from 'dict'."""
        self._keys = {}
        self._dict = {}
        if (len(args) + len(kwargs)) > 0:
            self.update(dict(*args, **kwargs))

    def __getitem__(self, k):
        """Retrieve the value associated with 'key' (in any case)."""
        return self._dict[self._keys[lower(k)]]

    def __setitem__(self, k, v):
        """Associate 'value' with 'key'. If 'key' already exists, but
        in different case, it will be replaced."""
        self._keys[lower(k)] = k
        self._dict[k] = v

    def has_key(self, k):
        """Case insensitive test wether 'key' exists."""
        return self._keys.has_key(lower(k))

    def get(self, k, d = None):
        """Retrieve value associated with 'key' or return default value
        if 'key' doesn't exist."""
        if self._keys.has_key(lower(k)):
            return self._dict.get(self._keys[lower(k)], d)
        else:
            return d

    def setdefault(self, key, default):
        """If 'key' doesn't exists, associate it with the 'default' value.
        Return value associated with 'key'."""
        if not self.has_key(key):
            self[key] = default
        return self[key]

    def update(self, d):
        """Copy (key,value) pairs from 'd'."""
        self._keys.update(dict(zip(map(lower, d.keys()), d.keys())))
        self._dict.update(d)

    # The rest don't change.
    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

    def __repr__(self):
        return self._dict.__repr__()

    def __str__(self):
        return self._dict.__str__()

#KeyInsensitiveDict = dicti
