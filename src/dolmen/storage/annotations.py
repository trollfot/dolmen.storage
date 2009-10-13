# -*- coding: utf-8 -*-

import grokcore.component as grok
from dolmen.storage import IDelegatedStorage
from dolmen.storage import DelegatedStorage, BTreeStorage
from zope.component import getAdapter, queryAdapter
from zope.schema.fieldproperty import FieldProperty
from zope.annotation.interfaces import IAttributeAnnotatable, IAnnotations


class AnnotationStorage(DelegatedStorage, grok.Adapter):
    grok.baseclass()
    grok.context(IAttributeAnnotatable)
    
    def __init__(self, context):
        name = grok.name.bind().get(self) or 'dolmen.storage.default'
        annotations = IAnnotations(context)
        if name not in annotations:
            annotations[name] = BTreeStorage()
        self.storage = annotations[name]


_marker = object()

class AnnotationProperty(object):
    """A property using a delegated annotation storage.
    """
    def __init__(self, field, storage="", name=None):
        self._name = name or field.__name__
        self._field = field
        self._storage = storage
        
    def __get__(self, inst, klass):
        field = self._field.bind(inst)
        storage = getAdapter(inst.context, IDelegatedStorage, self._storage)
        value = storage.get(self._name, _marker)
        if value is _marker:
            field = self._field.bind(inst)
            value = getattr(field, 'default', _marker)
            if value is _marker:
                raise AttributeError(self._name)
        return value

    def __set__(self, inst, value):
        field = self._field.bind(inst)
        if field.readonly:
            raise ValueError(self._name, 'field is readonly')
        field.validate(value)
        storage = getAdapter(inst.context, IDelegatedStorage, self._storage)
        storage[self._name] = value

    def __getattr__(self, name):
        return getattr(self._field, name)
