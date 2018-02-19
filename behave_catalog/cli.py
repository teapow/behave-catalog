# -*- coding: utf-8 -*-
"""The entry point from the command line."""

from __future__ import absolute_import, unicode_literals

import inspect
import os
import shutil
import sys
from collections import OrderedDict

from behave import step_registry
from behave.configuration import Configuration
from behave.runner import Runner
from jinja2 import Environment, PackageLoader, select_autoescape

environment = Environment(
    loader=PackageLoader("behave_catalog", "static"),
    autoescape=select_autoescape(["html", "htm", "xml"])
)

DIRECTORY = "/Users/thomas/Desktop/catalog"
PATH = os.path.dirname(__file__)

# Keys
PHRASE = "phrase"
DOCSTRING = "docstring"
SOURCE = "source"
FILE = "file"
LINE = "line"
FUNC = "func"

# Step types
GIVEN = "given"
WHEN = "when"
THEN = "then"
STEP = "step"


def run(config):
    """Generate the report."""
    runner = Runner(config)
    runner.setup_paths()
    runner.load_step_definitions()

    steps = step_registry.registry.steps
    context = {"steps": get_context(steps)}

    template = environment.get_template("index.html")
    html = template.render(**context)

    # Copy the source files to the write directory.
    static_files = [
        "bootstrap.min.css",
        "bootstrap.min.js",
        "index.css",
        "index.html",
        "index.js",
        "jquery.debounce.min.js",
        "jquery.min.js",
        "popper.min.js",
    ]

    for static_file in static_files:
        shutil.copyfile(
            src=os.path.join(PATH, "static", static_file),
            dst=os.path.join(DIRECTORY, static_file),
        )

    with open(os.path.join(DIRECTORY, "index.html"), "wb") as index_file:
        index_file.write(html.encode('ascii', 'xmlcharrefreplace'))

    return 0


def get_context(steps):
    context = OrderedDict()
    for group in [GIVEN, WHEN, THEN, STEP]:
        step_list = format_steps(steps.get(group))
        context[group] = sorted(step_list, key=lambda x: x[PHRASE])

    return context


def format_steps(steps):
    return [get_step(step) for step in steps]


def get_step(step):
    return {
        PHRASE: step.string,
        DOCSTRING: inspect.getdoc(step.func),
        SOURCE: {
            FILE: inspect.getsourcefile(step.func),
            LINE: inspect.getsourcelines(step.func)[1],
            FUNC: step.func.__name__,
        },
    }


def main(args=None):
    config = Configuration(args)
    return run(config)


if __name__ == '__main__':
    sys.exit(main())
