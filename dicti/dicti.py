#!/usr/bin/env python2

# By Sami, packaged by Tom
# http://code.activestate.com/recipes/66315-case-insensitive-dictionary/

def lower(potentialstring):
    'Lowercase the potential string if possible'
    try:
        return potentialstring.lower()
    except AttributeError:
        return potentialstring

class dicti(dict):
    """Dictionary with case-insensitive keys.
    
    Keys are retained in their original form
    when queried with .keys() or .items().

    Implementation: An internal dictionary maps lowercase
    keys to the original keys. All key lookups are done
    against the lowercase keys, but all methods that expose
    keys to the user retrieve the original keys."""

#   def __class__(self):
#       return self._keys.__class__()

#   def __cmp__(self):
#       return self._keys.__cmp__()

    def __contains__(self):
        return self._keys.__contains__()

#   def __delattr__(self):
#       return self._keys.__delattr__()

#   def __delitem__(self):
#       return self._keys.__delitem__()

#   def __doc__(self):
#       return self._keys.__doc__()

#   def __eq__(self):
#       return self._keys.__eq__()

#   def __format__(self):
#       return self._keys.__format__()

#   def __ge__(self):
#       return self._keys.__ge__()

#   def __getattribute__(self):
#       return self._keys.__getattribute__()

    def __getitem__(self, k):
        """Retrieve the value associated with 'key' (in any case)."""
        return dict.__getitem__(self, self._keys[lower(k)])

#   def __gt__(self):
#       return self._keys.__gt__()

#   def __hash__(self):
#       return self._keys.__hash__()

    def __init__(self, *args, **kwargs):
        """Create an empty dictionary, or update from 'dict'."""
        self._keys = {}
        if len(args) == 1:
            self.update(args[0])
        elif len(kwargs) > 0:
            self.update(dict(*args, **kwargs))

#   def __iter__(self):
#       return self._keys.__iter__()

#   def __le__(self):
#       return self._keys.__le__()

#   def __len__(self):
#       return self._keys.__len__()

#   def __lt__(self):
#       return self._keys.__lt__()

#   def __ne__(self):
#       return self._keys.__ne__()

#   def __new__(self):
#       return self._keys.__new__()

#   def __reduce__(self):
#       return self._keys.__reduce__()

#   def __reduce_ex__(self):
#       return self._keys.__reduce_ex__()

#   def __repr__(self):
#       return self._keys.__repr__()

#   def __setattr__(self):
#       return self._keys.__setattr__()

    def __setitem__(self, k, v):
        """Associate 'value' with 'key'. If 'key' already exists, but
        in different case, it will be replaced."""
        self._keys[lower(k)] = k
        dict.__setitem__(self, k, v)

#   def __sizeof__(self):
#       return self._keys.__sizeof__()

#   def __str__(self):
#       return self._keys.__str__()

#   def __subclasshook__(self):
#       return self._keys.__subclasshook__()

#   def clear(self):
#       return self._keys.clear()

#   def copy(self):
#       return self._keys.copy()

#   def fromkeys(self):
#       return self._keys.fromkeys()

    def get(self, k, d = None):
        """Retrieve value associated with 'key' or return default value
        if 'key' doesn't exist."""
        if self._keys.has_key(lower(k)):
            return dict.get(self, self._keys[lower(k)], d)
        else:
            return d

    def has_key(self, k):
        """Case insensitive test wether 'key' exists."""
        return self._keys.has_key(lower(k))

#   def items(self):
#       return self._keys.items()

#   def iteritems(self):
#       return self._keys.iteritems()

#   def iterkeys(self):
#       return self._keys.iterkeys()

#   def itervalues(self):
#       return self._keys.itervalues()

#   def keys(self):
#       return self._keys.keys()

#   def pop(self):
#       return self._keys.pop()

#   def popitem(self):
#       return self._keys.popitem()

    def setdefault(self, key, default):
        """If 'key' doesn't exists, associate it with the 'default' value.
        Return value associated with 'key'."""
        if not self.has_key(key):
            self[key] = default
        return self[key]

    def update(self, d):
        """Copy (key,value) pairs from 'd'."""
        self._keys.update(dict(zip(map(lower, d.keys()), d.keys())))
        dict.update(self, d)

#   def values(self):
#       return self._keys.values()

#   def viewitems(self):
#       return self._keys.viewitems()

#   def viewkeys(self):
#       return self._keys.viewkeys()

#   def viewvalues(self):
#       return self._keys.viewvalues()


#KeyInsensitiveDict = dicti
