from atelier.fablib import *

setup_from_fabfile(globals(), 'commondata.be')

env.revision_control_system = 'git'
env.doc_trees = []
