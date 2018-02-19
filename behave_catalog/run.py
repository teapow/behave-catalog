# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import shutil

from behave import step_registry
from jinja2 import Environment, PackageLoader, select_autoescape

from . import constants as const
from .context import get_context

DIRECTORY = "/home/thomas/Desktop/catalog"
PATH = os.path.dirname(__file__)


def run(runner):
    """Generate the report."""
    environment = Environment(
        loader=PackageLoader("behave_catalog", "static"),
        autoescape=select_autoescape(["html", "htm", "xml"])
    )

    runner.setup_paths()
    runner.load_step_definitions()

    context = get_context(step_registry.registry.steps)

    template = environment.get_template(const.INDEX_FILE)
    html = template.render(**context)

    # Copy the source files to the write directory.
    for static_file in const.STATIC_FILES:
        shutil.copyfile(
            src=os.path.join(PATH, "static", static_file),
            dst=os.path.join(DIRECTORY, static_file),
        )

    with open(os.path.join(DIRECTORY, const.INDEX_FILE), "wb") as index_file:
        index_file.write(html.encode('ascii', 'xmlcharrefreplace'))

    return 0
