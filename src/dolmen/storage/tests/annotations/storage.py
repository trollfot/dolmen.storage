"""
============================
Annotation storage container
============================

Getting started
---------------

We boostrap out project by importing the basic dependencies and
initializing the annotation component::

  >>> from zope.annotation.attribute import AttributeAnnotations
  >>> from zope.component import provideAdapter
  >>> provideAdapter(AttributeAnnotations)

Then, grokking the module will allow us to register our components
using Grok::

  >>> import grokcore.component as grok
  >>> from grokcore.component import testing
  >>> testing.grok(__name__)


  >>> from zope.interface import implements
  >>> from zope.annotation.interfaces import IAttributeAnnotatable

  >>> class Mammoth(object):
  ...    '''A furry creature
  ...    '''
  ...    implements(IAttributeAnnotatable)


  >>> from dolmen.storage import AnnotationStorage

  >>> class NamedStorage(AnnotationStorage):
  ...    grok.name('manfred')

  >>> class BaseStorage(AnnotationStorage):
  ...    pass

  >>> testing.grok_component('manfred', NamedStorage)
  True
  >>> testing.grok_component('anonymous', BaseStorage)
  True

  
  >>> from zope.component import getAdapter
  >>> from dolmen.storage import AnnotationStorage, IDelegatedStorage

  >>> manfred = Mammoth()
  >>> base_storage = IDelegatedStorage(manfred)
  >>> base_storage
  <dolmen.storage.tests.annotations.storage.BaseStorage object at ...>
  >>> base_storage.storage['test'] = object()
  >>> list(manfred.__annotations__.keys())
  ['dolmen.storage.default']

"""
