from atelier.tasks import ns, setup_from_tasks

setup_from_tasks(globals(), "commondata.be")
ns.configure({
    'revision_control_system': 'git',
    'docs': [],
})
