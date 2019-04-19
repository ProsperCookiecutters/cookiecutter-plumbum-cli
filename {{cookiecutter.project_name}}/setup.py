# Author: {{cookiecutter.author_name}}
# GENERATED: cookiecutter-plumbum-cli:{{cookiecutter.template_version}} {% now 'utc', '%Y-%m-%d' %}
"""packaging information for {{cookiecutter.project_name}}"""

import codecs
import os
from setuptools import setup, find_packages

__package_name__ = '{{cookiecutter.project_name}}'
__library_name__ = '{{cookiecutter.import_name}}'
__version__ = os.environ.get('VERSION', '0.0.0')

with codecs.open('README.{{cookiecutter.docs_filetype}}', 'r', 'utf-8') as readme_fh:
    __readme__ = readme_fh.read()

with open(os.path.join(__library_name__, 'VERSION'), 'w') as version_fh:
    version_fh.write(__version__.strip())

setup(
    name=__package_name__,
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    version=__version__,
    packages=find_packages(),
    description='{{cookiecutter.project_brief}}',
    long_description=__readme__,
    python_requires='>=3.6',
    {%- if cookiecutter.docs_filetype == 'md' %}
    long_description_content_type='text/markdown',
    {%- endif %}
    package_data={__library_name__: ['VERSION']},
    install_requires=['plumbum'],
    extras_require={
        'dev': ['tox', 'tox-pyenv', 'sphinx', 'black', 'twine'
            {%- if cookiecutter.docs_filetype == 'md' -%}
            , 'markdown']
            {%- elif cookiecutter.docs_filetype == 'rst' -%}
            , 'rstcheck']
            {%- endif %}
    },
    entry_points={
        'console_scripts': ['{{cookiecutter.cli_command}}={{cookiecutter.import_name}}.app:run_plumbum']
    },
)
