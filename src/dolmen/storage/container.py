# -*- coding: utf-8 -*-

from BTrees.OOBTree import OOBTree
from zope.event import notify
from zope.interface import implements
from zope.app.container import contained
from zope.exceptions import DuplicationError
from dolmen.storage import IStorage, IDelegatedStorage


class BTreeStorage(OOBTree):
    implements(IStorage)


class DelegatedStorage(object):
    implements(IDelegatedStorage)

    storage = None

    def __len__(self):
        return len(self.storage)

    def __setitem__(self, name, value):
        self.storage[name] = value

    def __getitem__(self, key, default=None):
        return self.storage[key]

    def get(self, key, default=None):
        return self.storage.get(key, default)

    def __delitem__(self, name):
        self.storage.__delitem__(name)
        
    def __iter__(self):
        return iter(self.storage)

    def __contains__(self, key):
        return self.storage.__contains__(key)

    has_key = __contains__

    def clear(self):
        return self.storage.clear()

    def keys(self):
        return self.storage.keys()

    def values(self):
        return self.storage.values()

    def items(self):
        return self.storage.items()
