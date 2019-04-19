# Author: John Purcell
# Email: jpurcell.ee@gmail.com
# (c) 2019

"""test cookiecutter with pytest-cookies"""
import os

import pytest
import plumbum
import markdown

# TODO: pathlib
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(HERE)
def find_bin_path():
    bin_path = os.path.join(ROOT, '.tox', os.environ['TOX_ENV_NAME'], 'bin')

    if not os.path.exists(bin_path):
        bin_path = os.path.join(ROOT, '.venv', 'bin')

    return bin_path

python = plumbum.local[os.path.join(find_bin_path(), 'python')]
black = plumbum.local[os.path.join(find_bin_path(), 'black')]
rstcheck = plumbum.local[os.path.join(find_bin_path(), 'rstcheck')]
virtualenv = plumbum.local[os.path.join(find_bin_path(), 'virtualenv')]

def test_build_markdown(cookies):
    result = cookies.bake(extra_context={'docs_filetype': 'md'})
    assert result.exit_code == 0

    with open(result.project.join('README.md'), 'r') as readme:
        markdown.markdown(readme.read())

def test_build_rst(cookies):
    result = cookies.bake(extra_context={'docs_filetype': 'rst'})
    assert result.exit_code == 0

    rstcheck(result.project.join('README.rst'))

def test_black(cookies):
    result = cookies.bake()

    black(result.project.join('setup.py'), '-S', '--check', '--diff', retcode=0)
    black(result.project.join('default_project_name'), '-S', '--check', '--diff', retcode=0)

@pytest.mark.slow
def test_sdist(cookies):
    result = cookies.bake()
    assert result.exit_code == 0

    with plumbum.local.cwd(result.project) as cwd:
        # Validate packaging
        py_result = python('setup.py', 'sdist')

        virtualenv('.tmpvenv')
        plumbum.local[cwd / '.tmpvenv/bin/python']('-m', 'ensurepip')
        venv_pip = plumbum.local[cwd / '.tmpvenv/bin/pip']

        # Validate `pip install`
        venv_pip('install', 'dist/DEFAULT-project-name-0.0.0.tar.gz')
        print(plumbum.local['ls'](cwd/ '.tmpvenv/bin'))

        # Validate cli/entry_points work
        my_cli = plumbum.local[cwd / '.tmpenv/bin/default-project-name']
