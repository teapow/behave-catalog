# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import inspect

from collections import OrderedDict
from datetime import datetime

from . import constants as const


def get_context(steps):
    return {
        "steps": get_context_steps(steps),
        "timestamp": datetime.now(),
    }


def get_context_steps(steps):
    """Return sorted lists of steps, grouped by the step type."""
    context = OrderedDict()
    for group in const.STEP_TYPES:
        step_list = format_steps(steps.get(group))
        context[group] = sorted(step_list, key=lambda x: x[const.PHRASE])

    return context


def format_steps(steps):
    return [get_step(step) for step in steps]


def get_step(step):
    return {
        const.PHRASE: step.string,
        const.DOCSTRING: inspect.getdoc(step.func),
        const.SOURCE: {
            const.FILE: inspect.getsourcefile(step.func),
            const.LINE: inspect.getsourcelines(step.func)[1],
            const.FUNC: step.func.__name__,
        },
    }
