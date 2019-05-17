VENV_FILE=.venv
WHICH_PYTHON=$(VENV_FILE)/bin/python
WHICH_PIP=$(VENV_FILE)/bin/pip
TOX_ENVLIST=py36,py37

clean:
	-@rm -rf $(VENV_FILE)
	-@rm -rf .eggs
	-@rm -rf *.egg-info
	-@find . -type d -maxdepth 3 -name "__pycache__" -print0 | xargs -0 rm -rv
	-@rm -rf .pytest_cache
	-@rm .coverage
	-@rm -rf .tox
	-@rm -rf DEFAULT-*

# TODO: Windows: https://stackoverflow.com/a/12099167
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
# https://github.com/pyenv/pyenv/issues/1219
CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" 
/usr/local/bin/pyenv:
	@brew update
	@brew install pyenv
${HOME}/.pyenv/versions/3.7.3: /usr/local/bin/pyenv
	-@pyenv install 3.7.3
${HOME}/.pyenv/versions/3.6.7: /usr/local/bin/pyenv
	-@pyenv install 3.6.7
else
${HOME}/.pyenv/versions/3.7.3: 
	-@pyenv install 3.7.3
${HOME}/.pyenv/versions/3.6.7: 
	-@pyenv install 3.6.7
endif

$(VENV_FILE):
	@virtualenv $(VENV_FILE) -p python3

$(VENV_FILE)/bin/black: $(VENV_FILE)
	@${WHICH_PIP} install black

$(VENV_FILE)/bin/cookiecutter: $(VENV_FILE)
	@${WHICH_PIP} install cookiecutter

$(VENV_FILE)/bin/tox: $(VENV_FILE)
	@$(WHICH_PIP) install tox
	@$(WHICH_PIP) install tox-pyenv

.PHONY: venv
venv: $(VENV_FILE) $(VENV_FILE)/bin/cookiecutter $(VENV_FILE)/bin/tox $(VENV_FILE)/bin/black

.PHONY: pyenv
pyenv:
	@pyenv local 3.7.3
	@pyenv local 3.6.7
	@eval "$(pyenv init -)"

.PHONY: build
build: $(VENV_FILE)/bin/cookiecutter
	-@rm -rf DEFAULT-*
	@$(VENV_FILE)/bin/cookiecutter . --no-input

.PHONY: test
test: venv  
	@$(VENV_FILE)/bin/tox -e $(TOX_ENVLIST) ${TOX_ARGS} -- -n 4

.PHONY: fast
fast: venv pyenv
	@$(VENV_FILE)/bin/tox -e $(TOX_ENVLIST) ${TOX_ARGS} -- -m "not slow"