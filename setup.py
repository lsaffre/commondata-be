from setuptools import setup

SETUP_INFO = dict(
    name='commondata.be',
    version='0.0.1',
    install_requires=[],
    description="Common knowledge about Belgium",
    license='GPL',
    test_suite='tests',
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://commondata.lino-framework.org",
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: GNU General Public License (GPL)
Natural Language :: English
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description=file('README.rst').read())

SETUP_INFO.update(packages=[str(n) for n in """
commondata.be
""".splitlines() if n])

SETUP_INFO.update(namespace_packages=['commondata'])

setup(**SETUP_INFO)