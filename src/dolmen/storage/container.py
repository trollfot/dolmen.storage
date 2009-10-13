# -*- coding: utf-8 -*-

from BTrees.OOBTree import OOBTree
from zope.interface import implements
from dolmen.storage import IStorage, IDelegatedStorage


class BTreeStorage(OOBTree):
    implements(IStorage)


class DelegatedStorage(object):
    implements(IDelegatedStorage)

    storage = None

    def __len__(self):
        return len(self.storage)

    def __set__(self, name, value):
        self.storage[name] = value
    __setitem__ = __set__

    def __get__(self, key, default=None):
        return self.storage.get(key, default)
    get = __getitem__ = __get__

    def __delitem__(self, name):
        return self.storage.__delitem__(name)

    def __iter__(self):
        return self.storage.__iter__()

    def __contains__(self, key):
        return self.storage.__contains__(key)

    def clear(self):
        return self.storage.clear()

    def keys(self):
        return self.storage.keys()

    def values(self):
        return self.storage.values()

    def items(self):
        return self.storage.items()
