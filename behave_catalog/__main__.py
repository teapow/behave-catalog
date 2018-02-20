# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import argparse
import os
import sys

from behave import step_registry
from behave.configuration import Configuration
from behave.runner import Runner

from .constants import DEFAULT_DIR
from .run import run

default_dir = os.path.join(os.getcwd(), DEFAULT_DIR)

parser = argparse.ArgumentParser(
    description='Generate a HTML report listing all gherkin step definitions '
                'discovered by behave.')

parser.add_argument(
    'path', type=str, nargs='?', default=default_dir,
    help='Path to the directory where the generated report will be placed. '
         'Defaults to: {dir}.'.format(dir=default_dir),
)


def main():
    """Entry point."""
    path = parser.parse_args().path

    config = Configuration(command_args={})
    runner = Runner(config)
    runner.setup_paths()
    runner.load_step_definitions()

    exit_code = run(steps=step_registry.registry.steps, output_to=path)
    return sys.exit(exit_code)


if __name__ == '__main__':
    main()
