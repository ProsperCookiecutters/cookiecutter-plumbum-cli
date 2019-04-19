# cookiecutter-plumbum-cli
Template for creating CLI's with Plumbum

[Plumbum](https://plumbum.readthedocs.io/en/latest/cli.html) provides a powerful and extensible CLI framework along with a `subprocess` wrapper for terminal operations.  A perfect tool for building the myriad little-things in modern infrastructure.

## Getting Started

Install [Cookiecutter](https://github.com/audreyr/cookiecutter) and generate a new pytest plugin project:

```no-highlight
$ pip install cookiecutter
$ cookiecutter https://github.com/ProsperCookiecutters/cookiecutter-plumbum-cli
```

## Usage 

```no-highlight
project_name [DEFAULT-project-name]: name of github project
import_name [default_project_name]: name for `import`
cli_command [default-project-name]: (kebab-case preferred) terminal cli command
project_brief [brief description of what your project is for]: 
author_name [Jane Doe]: 
author_email [fake@fake.com]: 
github_username [fakegithub]: 
Select docs_filetype:
1 - md
2 - rst
Choose from 1, 2 (1, 2) [1]: 
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0
4 - Apache Software License 2.0
5 - Mozilla Public License 2.0
Choose from 1, 2, 3, 4, 5 (1, 2, 3, 4, 5) [1]: 
tox_pyenvs [py37,py36]: template supports >=3.6
template_version [1.0.0]: DO NOT CHANGE
```

It is easier to build 10 small things rather than 1 big one.  Every time there's a cron job, or small [Automate The Boring Stuff]() app, or a data scraper -- this template is meant to give you an easy to use/extend `main()` framework to build off.  Additionally, [Plumbum](https://plumbum.readthedocs.io/en/latest) provides a platform agnostic tool to use terminal commands.


## Features

NOTE: it's not a Buffalo -- you don't have to use every part.  This template is meant to cover as many bases as possible.  

- [Plumbum](https://plumbum.readthedocs.io/en/latest/cli.html) CLI application.  
- Makefile to simplify CI/CD work
- Plans for
    - Releasing to PyPI
    - Testing with [tox](https://tox.readthedocs.io/en/latest/index.html)
- Python `logging` integration instead of `print()` 
- Style validation with [Black](https://github.com/ambv/black)
- ReadTheDocs with [Sphinx]()

## Testing

```bash
make test
```

Powered by [pytest-cookies](https://github.com/hackebrot/pytest-cookies) and [plumbum](https://plumbum.readthedocs.io/en/latest/cli.html)

## Contributing

TODO

