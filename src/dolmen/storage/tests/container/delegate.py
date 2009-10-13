"""
=================
Delegated Storage
=================

`dolmen.storage` provides a couple of useful storage containers. The
second one is a delegated storage component. `DelegatedStorage` is a
component delegating all the container related method to a `storage`,
which is an object implementing `IStorage`.

We first create a DelegatedStorage::

  >>> from dolmen.storage import IStorage, BTreeStorage, DelegatedStorage
  
  >>> class MyStorage(DelegatedStorage):
  ...     def __init__(self):
  ...         self.storage = BTreeStorage()

  >>> container = MyStorage()


We ensure that the interface is correctly provided::

  >>> IStorage.providedBy(container)
  True
  >>> IStorage.providedBy(container.storage)
  True


In order to enforce the consistency of our declaration, we check the
implementation in depth, using verifyObject::

  >>> from zope.interface.verify import verifyObject
  >>> verifyObject(IStorage, container)
  True


Let's have some basic tests, to check that everything works as
intended::

  >>> container['test'] = 'something'
  >>> len(container)
  1

  >>> container['test']
  'something'

  >>> list(container.values())
  ['something']

  >>> list(container.keys())
  ['test']

  >>> list(container.items())
  [('test', 'something')]
  
  >>> for i in container: print repr(i)
  'test'

  >>> 'test' in container
  True

  >>> container.clear()
  >>> len(container)
  0

  >>> container['james'] = object()
  >>> print container.get('james')
  <object object at ...>

  >>> print container.get('judith')
  None

  >>> del container['james']
  >>> print container['james']
  None
  >>> len(container)
  0

"""
