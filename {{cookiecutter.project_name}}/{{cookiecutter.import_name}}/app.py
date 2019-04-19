# Author: {{cookiecutter.author_name}}
# GENERATED: cookiecutter-plumbum-cli:{{cookiecutter.template_version}} {% now 'utc', '%Y-%m-%d' %}

"""Plumbum.cli application file"""

import logging
import logging.handlers
import os
import sys

from plumbum import cli

HERE = os.path.abspath(os.path.dirname(__file__))
_PROGNAME = '{{cookiecutter.project_name}}'
try:
    with open(os.path.join(HERE, 'VERSION')) as version_fh:
        _VERSION = version_fh.read().strip()
except Exception:
    _VERSION = 'UNKOWN'


class {{ cookiecutter.cli_command | replace('-', ' ') | replace('_', ' ') | title | replace(' ', '')}}(cli.Application):
    PROGNAME = _PROGNAME
    VERSION = _VERSION

    verbose_stream = sys.stdout

    debug = cli.Flag(['d', '--debug'], help='enable debug mode')
    verbose = cli.Flag(['v', '--verbose'], help='enable verbose logging')

    log_dir = cli.SwitchAttr(
        ['--log-dir'],
        str,
        help='logging output directory',
        default=os.environ.get('LOG_DIR', ''),
    )
    log_level = cli.SwitchAttr(
        ['--log-level'],
        cli.Set('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'),
        help='Logging reporting default',
        default=os.environ.get('LOG_LEVEL', 'INFO'),
    )
    _logger = None

    @property
    def logger(self):
        if self._logger:
            return self._logger

        self._logger = logging.getLogger(self.PROGNAME)
        formatter = logging.Formatter(
            '[%(levelname)s:%(filename)s--%(funcName)s:%(lineno)s] %(message).1000s'
        )

        if self.debug:
            self._logger.setLevel('DEBUG')
        else:
            self._logger.setLevel(self.log_level)

        handler = logging.handlers.TimedRotatingFileHandler(
            os.path.join(self.log_dir, f'{self.PROGNAME}.log')
        )
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)

        if self.verbose:
            v_handler = logging.StreamHandler()
            v_handler.setFormatter(formatter)
            self._logger.addHandler(v_handler)

        return self._logger

    def main(self):
        """project main goes here"""
        self.logger.info('HELLO WORLD')


def run_plumbum():
    """entry_points['console_scripts'] hook to launch Plumbum"""
    {{ cookiecutter.cli_command | replace('-', ' ') | replace('_', ' ') | title | replace(' ', '')}}.run()


if __name__ == '__main__':
    run_plumbum()
