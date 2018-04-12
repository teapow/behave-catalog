==============
behave-catalog
==============

.. contents:: Table of contents

Background
==========

`Gherkin`_ is a language that enables non-technical members of a team to clearly and concisely define the behaviour of a given feature before it's implemented. `Behave`_ works beside Gherkin to support this behaviour-driven development style.

The problem to solve
--------------------

Over time, a team may build-up a catalog of steps that, if reused, can cut down the amount time it takes for feature tests to be written. *But, how can this catalog of pre-existing steps be exposed to non-technical team members?*

Alternate solutions
-------------------

* **Give them access to the source code?**

      This requires knowledge of where the steps themselves are defined within the source. You need to know where to look, and what you're looking for.

* **Keep a copy of the steps in another external document (such as Confluence / Google Drive / Dropbox)?**

      It doesn't take much for this to fall behind the actual step definitions, and it's an additional overhead that needs to be manually managed.

* **Can't behave already do this?**

      `Yes it can`_, but remember; these are non-technical staff who are afraid of the terminal (plus, they'll need to be set up with a local development environment).

Introducing behave-catalog
--------------------------

`behave-catalog`_ solves this problem by generating a single, searchable HTML document that shows all step definitions, along with how to use them, grouped by `GIVEN`, `WHEN`, `THEN` (and `STEP`).

You could automatically generate this document as part of your build-pipeline, and host it to make easily accessible, and crucially, always up-to-date.


Quickstart
==========

.. code-block::

    $ pip install behave-catalog
    $ behave-catalog

``behave-catalog`` automatically detect all steps (that are discoverable by ``behave``), and will create a new directory within the same directory from which ``behave-catalog`` was invoked. Open ``behave-catalog/index.html`` in a browser to view the generated document.


Advanced usage
==============

For a full listing of flags/command-line options, use the ``--help`` flag. Some common use-cases are described below.

Overriding the default output directory
---------------------------------------

The default output directory can be overridden as follows:

.. code-block::

    $ behave-catalog --path=<dir>

Passing command-line arguments through to behave
------------------------------------------------

You can pass `command-line arguments`_ through to ``behave`` by providing a string as follows:

.. code-block::

    $ behave-catalog --command-args="--tags=tag1,tag2,-tag3"


.. _behave: https://github.com/behave/behave
.. _behave-catalog: https://github.com/teapow/behave-catalog
.. _command-line arguments: http://behave.readthedocs.io/en/latest/behave.html#command-line-arguments
.. _gherkin: https://github.com/cucumber/cucumber/wiki/Gherkin
.. _yes it can: http://behave.readthedocs.io/en/latest/behave.html#cmdoption-steps-catalog