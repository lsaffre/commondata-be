# -*- coding: UTF-8 -*-
from setuptools import setup

SETUP_INFO = dict(
    name='commondata.be',
    version='0.0.2',  # released 20160822
    install_requires=['commondata'],
    description="Common data about Belgium",
    license='GPL',
    test_suite='tests',
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="https://github.com/lsaffre/commondata-be",
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description="""\
`Common data <https://github.com/lsaffre/commondata>`_ about
Belgium, freely available and maintained in Python.

This currently includes a list of Belgian places in multiple languages
with zip codes.

DISCLAIMER: This comes with no warranty at all.  We are still
discussing whether this package is meaningful.

Usage example:

>>> from commondata.be.places import root
>>> belgium = root()
>>> print(', '.join([x.fr for x in belgium.children]))
Bruxelles, Région flamande, Région wallonne
>>> print(', '.join([x.nl for x in belgium.children]))
Brussel, Vlaams Gewest, Wallonië
>>> wallonia = belgium.children[2]
>>> print(', '.join([x.fr for x in wallonia.children]))
Namur, Liège, Hainaut, Limbourg, Brabant wallon
>>> print(', '.join([x.nl for x in wallonia.children]))
Namen, Luik, Henegouwen, Limburg, Waals-Brabant

The following number will decrease when we continue to change "city"
entries into "village" or "township" entries:

>>> liege = wallonia.children[1]
>>> len(liege.children)
353
>>> eupen = liege.get(fr="Eupen")
>>> print(eupen.zip_code)
4700

""")

SETUP_INFO.update(packages=[str(n) for n in """
commondata.be
""".splitlines() if n])

SETUP_INFO.update(namespace_packages=['commondata'])

if __name__ == '__main__':
    setup(**SETUP_INFO)
