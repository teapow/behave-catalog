# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os
import shutil

from jinja2 import Environment, PackageLoader, select_autoescape

from . import __BASE_DIR__
from . import constants as const
from .context import get_template_context


def run(steps, output_to):
    """Generate the report."""

    # Create the output_to dir if it doesn't already exist.
    if not os.path.exists(output_to):
        os.makedirs(output_to)

    environment = Environment(
        loader=PackageLoader("behave_catalog", "static"),
        autoescape=select_autoescape(["html", "htm", "xml"]),
    )

    context = get_template_context(steps)
    template = environment.get_template(const.INDEX_FILE)
    html = template.render(**context)

    # Copy the source files to the write directory.
    for static_file in const.STATIC_FILES:
        shutil.copyfile(
            src=os.path.join(__BASE_DIR__, "static", static_file),
            dst=os.path.join(output_to, static_file),
        )

    with open(os.path.join(output_to, const.INDEX_FILE), "wb") as index_file:
        index_file.write(html.encode('ascii', 'xmlcharrefreplace'))

    return 0
