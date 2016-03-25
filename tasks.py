from atelier.tasks import ns
ns.setup_from_tasks(globals(), "commondata.be")
ns.configure({
    'revision_control_system': 'git',
    'docs': [],
})
