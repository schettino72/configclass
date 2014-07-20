from doitpy.pyflakes import Pyflakes


DOIT_CONFIG = {'default_tasks': ['pyflakes']}


def task_pyflakes():
    yield Pyflakes().tasks('**/*.py')

def task_test():
    return {
        'actions': ['py.test'],
        'file_dep': ['configclass.py', 'test_configclass.py'],
        }

def task_coverage():
    return {
        'actions': [
            'coverage run `which py.test`',
            'coverage report --include=configclass.py,test_configclass.py'],
        'verbosity': 2,
        }




def task_manifest():
    """create manifest file for distutils """

    cmd = "git ls-tree --name-only -r HEAD > MANIFEST"
    return {'actions': [cmd]}


def task_pypi():
    """upload package to pypi"""
    return {
        'actions': ["python setup.py sdist upload"],
        'task_dep': ['manifest'],
        }
