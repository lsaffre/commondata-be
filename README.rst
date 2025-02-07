=============================
The ``commondata.be`` package
=============================

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
