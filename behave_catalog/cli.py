# -*- coding: utf-8 -*-
"""The entry point from the command line."""

from __future__ import absolute_import, unicode_literals

import sys

from behave.configuration import Configuration
from behave.runner import Runner

from .run import run


def main(args=None):
    config = Configuration(args)
    runner = Runner(config)
    return run(runner)


if __name__ == '__main__':
    sys.exit(main())
