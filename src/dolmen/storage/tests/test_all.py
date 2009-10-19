# -*- coding: utf-8 -*-

import unittest
from pkg_resources import resource_listdir
from zope.testing import doctest, cleanup, module
from zope.app.testing import functional

ftesting_zcml = os.path.join(os.path.dirname(__file__), 'ftesting.zcml')
FunctionalLayer = functional.ZCMLLayer(
    ftesting_zcml, __name__, 'FunctionalLayer', allow_teardown=True)


def setUpZope(test):
    zope.component.eventtesting.setUp(test)

def cleanUpZope(test):
    cleanup.cleanUp()

def suiteFromPackage(name):
    files = resource_listdir(__name__, name)
    suite = unittest.TestSuite()
    for filename in files:
        if not filename.endswith('.py'):
            continue
        if filename.endswith('_fixture.py'):
            continue
        if filename == '__init__.py':
            continue

        dottedname = 'dolmen.storage.tests.%s.%s' % (name, filename[:-3])
        test = doctest.DocTestSuite(
            dottedname,
            setUp=setUpZope,
            tearDown=cleanUpZope,
            optionflags=doctest.ELLIPSIS+doctest.NORMALIZE_WHITESPACE)
        suite.addTest(test)
    return suite


def test_suite():
    suite = unittest.TestSuite()

    readme = functional.FunctionalDocFileSuite(
        'README.txt',
        optionflags=(doctest.ELLIPSIS + doctest.NORMALIZE_WHITESPACE),
        )
    readme.layer = FunctionalLayer
    suite.addTest(readme)
    
    for name in ['container', 'annotations']:
        suite.addTest(suiteFromPackage(name))
    
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
