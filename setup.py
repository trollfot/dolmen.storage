from setuptools import setup, find_packages
from os.path import join

name = 'dolmen.storage'
version = '0.1'
readme = open(join('dolmen', 'storage', 'README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read().replace(name + ' - ', '')

setup(name = name,
      version = version,
      description = 'Dolmen Zope3 Storage',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'Grok Zope3 CMS Dolmen',
      author = 'Souheil Chelfouh',
      author_email = 'souheil@chelfouh.com',
      url = 'http://tracker.trollfot.org/',
      download_url = 'http://pypi.python.org/pypi/dolmen.storage',
      license = 'GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages = ['dolmen'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = True,
      install_requires=[
          'setuptools',
          'grok',
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Grok',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
