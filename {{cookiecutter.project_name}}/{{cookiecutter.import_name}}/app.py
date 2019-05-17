# Author: {{cookiecutter.author_name}}
# GENERATED: cookiecutter-plumbum-cli:{{cookiecutter.template_version}} {% now 'utc', '%Y-%m-%d' %}

"""Plumbum.cli application file"""

import logging
import os
import sys

from plumbum import cli
from . import exceptions

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

    def init_logger(self):
        """build a basicConfig logger for project"""
        if self.debug:
            logging.basicConfig(
                format='[%(levelname)s:%(filename)s--%(funcName)s:%(lineno)s] %(message)s',
                level=self.log_level,
                stream=self.verbose_stream
            )
        else:
            logging.basicConfig(
                format='[%(levelname)s:%(filename)s--%(funcName)s:%(lineno)s] %(message)s',
                level=self.log_level,
                stream=self.verbose_stream
            )

    def main(self):
        """project main goes here"""
        self.init_logger()  # MAGIC -- DO NOT DELETE <3
        logging.info('HELLO WORLD')


def run_plumbum():
    """entry_points['console_scripts'] hook to launch Plumbum"""
    {{ cookiecutter.cli_command | replace('-', ' ') | replace('_', ' ') | title | replace(' ', '')}}.run()


if __name__ == '__main__':
    run_plumbum()
