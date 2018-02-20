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
    '--path',
    '-p',
    type=str,
    nargs='?',
    default=default_dir,
    help='Path to the directory where the generated report will be placed. '
         'Defaults to: {dir}.'.format(dir=default_dir),
)

parser.add_argument(
    '--command-args',
    '-b',
    type=str,
    nargs='?',
    default='',
    dest='command_args',
    help='Arguments to pass through to the underlying behave runner, as '
         'a quoted string.',
)


def main():
    """Entry point."""
    args = parser.parse_args()
    config = Configuration(args.command_args)
    runner = Runner(config)

    with runner.path_manager:
        runner.setup_paths()
        runner.load_step_definitions()  # This populates the step_registry.

    exit_code = run(steps=step_registry.registry.steps, output_to=args.path)
    return sys.exit(exit_code)


if __name__ == '__main__':
    main()
