VENV_FILE=.venv
WHICH_PYTHON=$(VENV_FILE)/bin/python
WHICH_PIP=$(VENV_FILE)/bin/pip

clean:
	-@rm -rf $(VENV_FILE)
	-@rm -rf .eggs
	-@rm -rf *.egg-info
	-@find . -type d -maxdepth 3 -name "__pycache__" -print0 | xargs -0 rm -rv
	-@rm -rf .pytest_cache
	-@rm .coverage
	-@rm -rf .tox
	-@rm -rf DEFAULT-*

$(VENV_FILE):
	@virtualenv $(VENV_FILE) -p python3

$(VENV_FILE)/lib/python*/site-packages/cookiecutter/: $(VENV_FILE)
	@${WHICH_PIP} install cookiecutter

$(VENV_FILE)/lib/python*/site-packages/tox/: $(VENV_FILE)
	@$(WHICH_PIP) install tox
	@$(WHICH_PIP) install tox-pyenv

.PHONY: venv
venv: $(VENV_FILE) $(VENV_FILE)/lib/python*/site-packages/cookiecutter/ $(VENV_FILE)/lib/python*/site-packages/tox/

.PHONY: build
build: venv
	-@rm -rf DEFAULT-*
	@cookiecutter . --no-input