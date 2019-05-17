# Author: John Purcell
# Email: jpurcell.ee@gmail.com
# (c) 2019

"""test cookiecutter with pytest-cookies"""
import os
import re

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
    """basic build test"""
    result = cookies.bake(extra_context={'docs_filetype': 'md'})
    assert result.exit_code == 0

    with open(result.project.join('README.md'), 'r') as readme:
        markdown.markdown(readme.read())

def test_build_rst(cookies):
    """build with .rst docs"""
    result = cookies.bake(extra_context={'docs_filetype': 'rst'})
    assert result.exit_code == 0

    rstcheck(result.project.join('README.rst'))

def test_black(cookies):
    """validate that all generated code is Black by default"""
    result = cookies.bake()

    black(result.project.join('setup.py'), '-S', '--check', '--diff', retcode=0)
    black(result.project.join('default_project_name'), '-S', '--check', '--diff', retcode=0)

@pytest.mark.slow
def test_sdist(cookies):
    """make sure project can build tar for release"""
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

@pytest.mark.slow
def test_makefile(cookies):
    """validate makefile commands run without error"""
    result = cookies.bake(
        extra_context={'tox_pyenvs': os.environ.get('TOX_ENV_NAME', 'py37')}
    )
    with plumbum.local.cwd(result.project) as cwd:
        make = plumbum.local['make']

        black = make('black', '$BLACK_ARGS="--check"')
        print(black)
        build = make('build')
        print(build)
        install = make('install')
        print(install)
        test = make('test')
        print(test)

def test_cleanup(cookies):
    """makes sure all _{pattern} directories have been cleaned out of resuts"""
    result = cookies.bake()

    with plumbum.local.cwd(result.project) as cwd:
        for filename in [x.name for x in cwd.list()]:
            assert not re.match(r'^_', filename)

