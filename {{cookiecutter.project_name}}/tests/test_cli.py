# Author: {{cookiecutter.author_name}}
# GENERATED: cookiecutter-plumbum-cli:{{cookiecutter.template_version}} {% now 'utc', '%Y-%m-%d' %}
"""tests for live-cli interface"""
import os
import plumbum

# TODO: pathlib
HERE = os.path.abspath(os.path.dirname(__file__))
ROOT = os.path.dirname(HERE)
def find_bin_path():
    bin_path = os.path.join(ROOT, '.tox', os.environ['TOX_ENV_NAME'], 'bin')

    if not os.path.exists(bin_path):
        bin_path = os.path.join(ROOT, '.venv', 'bin')

    return bin_path

python = plumbum.local[os.path.join(find_bin_path(), 'python')]
virtualenv = plumbum.local[os.path.join(find_bin_path(), 'virtualenv')]

def test_hello_world():
    assert True
