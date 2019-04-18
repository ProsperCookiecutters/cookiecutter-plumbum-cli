# cookiecutter-plumbum-cli
Template for creating CLI's with Plumbum

[Plumbum](https://plumbum.readthedocs.io/en/latest/cli.html) provides a powerful and extensible CLI framework along with a `subprocess` wrapper for terminal operations.  A perfect tool for building the myriad little-things in modern infrastructure.

## Usage 

TODO

## Features

- [Plumbum](https://plumbum.readthedocs.io/en/latest/cli.html) CLI application.  
- Docker container to run CLI anywhere
- Makefile to simplify CI/CD work
- Plans for
    - Releasing to PyPI
    - Releasing to a docker registry
    - Testing with [tox](https://tox.readthedocs.io/en/latest/index.html)
- Log errors to chat program (slack/discord/hipchat) c/o [ProsperCommon]()
- Style validation with [Black](https://github.com/ambv/black)

## Testing

```bash
tox
```

Powered by [pytest-cookies](https://github.com/hackebrot/pytest-cookies) and [plumbum](https://plumbum.readthedocs.io/en/latest/cli.html)

## Contributing

TODO

