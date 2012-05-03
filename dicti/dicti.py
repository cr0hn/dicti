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
        if len(args) == 1:
            self.update(args[0])
        elif len(kwargs) > 0:
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
    def __class__(self):
        return self._dict.__class__()

    def __cmp__(self):
        return self._dict.__cmp__()

    def __contains__(self):
        return self._dict.__contains__()

    def __delattr__(self):
        return self._dict.__delattr__()

    def __delitem__(self):
        return self._dict.__delitem__()

    def __doc__(self):
        return self._dict.__doc__()

    def __eq__(self):
        return self._dict.__eq__()

    def __format__(self):
        return self._dict.__format__()

    def __ge__(self):
        return self._dict.__ge__()

    def __getattribute__(self):
        return self._dict.__getattribute__()

    def __getitem__(self):
        return self._dict.__getitem__()

    def __gt__(self):
        return self._dict.__gt__()

    def __hash__(self):
        return self._dict.__hash__()

#   def __init__(self):
#       return self._dict.__init__()

    def __iter__(self):
        return self._dict.__iter__()

    def __le__(self):
        return self._dict.__le__()

    def __len__(self):
        return self._dict.__len__()

    def __lt__(self):
        return self._dict.__lt__()

    def __ne__(self):
        return self._dict.__ne__()

    def __new__(self):
        return self._dict.__new__()

    def __reduce__(self):
        return self._dict.__reduce__()

    def __reduce_ex__(self):
        return self._dict.__reduce_ex__()

    def __repr__(self):
        return self._dict.__repr__()

    def __setattr__(self):
        return self._dict.__setattr__()

    def __setitem__(self):
        return self._dict.__setitem__()

    def __sizeof__(self):
        return self._dict.__sizeof__()

    def __str__(self):
        return self._dict.__str__()

    def __subclasshook__(self):
        return self._dict.__subclasshook__()

    def clear(self):
        return self._dict.clear()

    def copy(self):
        return self._dict.copy()

    def fromkeys(self):
        return self._dict.fromkeys()

#   def get(self):
#       return self._dict.get()

#   def has_key(self):
#       return self._dict.has_key()

    def items(self):
        return self._dict.items()

    def iteritems(self):
        return self._dict.iteritems()

    def iterkeys(self):
        return self._dict.iterkeys()

    def itervalues(self):
        return self._dict.itervalues()

    def keys(self):
        return self._dict.keys()

    def pop(self):
        return self._dict.pop()

    def popitem(self):
        return self._dict.popitem()

    def setdefault(self):
        return self._dict.setdefault()

    def update(self):
        return self._dict.update()

    def values(self):
        return self._dict.values()

    def viewitems(self):
        return self._dict.viewitems()

    def viewkeys(self):
        return self._dict.viewkeys()

    def viewvalues(self):
        return self._dict.viewvalues()


#KeyInsensitiveDict = dicti
