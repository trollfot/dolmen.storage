==============
dolmen.storage
==============

`dolmen.storage` defines a clear high-level API to deal containment
storage.

Components
==========

Storage
-------

A storage is a component dedicated to store contents. It behaves like
a container and provides the interface `dolmen.storage.IStorage`.

Out of the box, two IStorage components are available, based on a ZODB
BTree::

  >>> from dolmen.storage import IStorage
  >>> from dolmen.storage import container
  >>> from zope.app.container.interfaces import IContainer

  >>> otree = container.OOBTreeStorage()
  >>> itree = container.IOBTreeStorage()

  >>> IStorage.extends(IContainer)
  True

  >>> from zope.interface import verify
  >>> verify.verifyObject(IStorage, otree)
  True
  >>> verify.verifyObject(IStorage, itree)
  True


Delegated storage
-----------------

A delegated storage 

>>> from dolmen.storage import IDelegatedStorage
