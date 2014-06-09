from os.path import join
# from atelier.test import TestCase

# ROOTDIR = join(__file__, '..')


# class DocTests(TestCase):
#     project_root = ROOTDIR
   
#     def test_docs(self):
#         self.run_simple_doctests('/README.rst')


from unittest import TestCase
import doctest


class DocTests(TestCase):

    def test_docs(self):
        doctest.testfile(join('..', "README.rst"), encoding="utf-8")
