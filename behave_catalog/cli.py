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

DIRECTORY = "/home/thomas/Desktop/catalog"
PATH = os.path.dirname(__file__)


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
        "index.html",
        "index.js",
        "jquery.min.js",
        "popper.min.js",
    ]

    for file in static_files:
        shutil.copyfile(
            src=os.path.join(PATH, "static", file),
            dst=os.path.join(DIRECTORY, file),
        )

    with open(os.path.join(DIRECTORY, "index.html"), "wb") as index_file:
        index_file.write(html.encode('ascii', 'xmlcharrefreplace'))

    return 0


def get_context(steps):
    context = OrderedDict()
    for group in ["given", "when", "then", "step"]:
        step_list = format_steps(steps.get(group))
        context[group] = sorted(step_list, key=lambda x: x["phrase"])

    return context


def format_steps(steps):
    return [get_step(step) for step in steps]


def get_step(step):
    return {
        "phrase": step.string,
        "docstring": inspect.getdoc(step.func),
        "source": {
            "file": inspect.getsourcefile(step.func),
            "line": inspect.getsourcelines(step.func)[1],
            "func": step.func.__name__,
        },
    }


def main(args=None):
    config = Configuration(args)
    return run(config)


if __name__ == '__main__':
    sys.exit(main())
