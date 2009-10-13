# -*- coding: utf-8 -*-

import grokcore.component as grok
from zope.annotation.interfaces import IAnnotations
from dolmen.storage import IDelegatedStorage
from dolmen.storage import DelegatedStorage, BtreeStorage


class AnnotationStorage(DelegatedStorage, grok.Adapter):
    grok.baseclass()
    grok.context(IAnnotatable)

    storage_key = u""
    
    def __init__(self, context):
        annotations = IAnnotations(context)
        if self.storage_key not in annotations:
            annotations[self.storage_key] = BtreeStorage()
        self.storage = annotations[self.storage_key]


class AnnotationProperty(object):
    """A property using a delegated annotation storage.
    """
    def __init__(self, field, storage="", name=None):
        self._name = name or field.__name__
        self._storage = storage
        self.__field = field

    def __get__(self, inst, klass):
        field = self.__field.bind(inst)
        storage = getAdapter(
            inst.context, IDelegatedStorage, self._storage
            )
        return storage[self._name]

    def __set__(self, inst, value):
        field = self.__field.bind(inst)
        if field.readonly:
            raise ValueError(self._name, 'field is readonly')
        storage = getAdapter(
            inst.context, IDelegatedStorage, self._storage
            )
        storage[self._name] = value

    def __getattr__(self, name):
        return getattr(self.__field, name)
