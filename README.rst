Whitespace
==========

.. image:: https://img.shields.io/pypi/v/whitespace.svg
    :target: https://pypi.python.org/pypi/whitespace

An interpreter written in `Python <https://www.python.org/>`_ for the imperative, stack based language called `Whitespace <https://en.wikipedia.org/wiki/Whitespace_(programming_language)>`_.

Installation
------------

Install it using:

.. code-block:: bash

    $ pip install whitespace

You would now have access to an executable called ``whitespace``. Type

.. code-block:: bash

    $ whitespace -h

to learn more.

Usage
-----

Let's say you've written a `Whitespace`_ program and stored it in the file ``program.ws``. Then, to execute that program, type:

.. code-block:: bash

    $ whitespace program.ws

You can find example `Whitespace`_ programs at `tests/fixtures <https://github.com/dwayne/whitespace-python/tree/master/tests/fixtures>`_. Be sure to run them to see what they do.

For example, here's the `factorial program <https://github.com/dwayne/whitespace-python/blob/master/tests/fixtures/fact.ws>`_ and a sample execution:

.. code-block:: bash

    $ whitespace fact.ws
    Enter a number: 40
    40! = 20397882081197443358640281739902897356800000000

Development
-----------

Get the source code.

.. code-block:: bash

    $ git clone git@github.com:dwayne/whitespace-python.git

Create a `virtual environment <https://docs.python.org/3/library/venv.html>`_ and activate it.

.. code-block:: bash

    $ cd whitespace-python
    $ pyvenv venv
    $ . venv/bin/activate

Then, upgrade ``pip`` and ``setuptools`` and install the development dependencies.

.. code-block:: bash

    (venv) $ pip install -U pip setuptools
    (venv) $ pip install -r requirements-dev.txt

You're now all set to begin development.

Testing
-------

Tests are written using the `unittest <https://docs.python.org/3/library/unittest.html>`_ unit testing framework.

Run all tests.

.. code-block:: bash

    (venv) $ python -m unittest

Run a specific test module.

.. code-block:: bash

    (venv) $ python -m unittest tests.test_parser

Run a specific test case.

.. code-block:: bash

    (venv) $ python -m unittest tests.test_parser.ParserTestCase

Run a specific test method.

.. code-block:: bash

    (venv) $ python -m unittest tests.test_parser.ParserTestCase.test_it_parses_push

References
----------

- `Whitespace tutorial <http://compsoc.dur.ac.uk/whitespace/tutorial.html>`_

Credits
-------

Thanks to Edwin Brady and Chris Morris for designing/developing this programming language (also developers of the `Idris <https://en.wikipedia.org/wiki/Idris_(programming_language)>`_ programming language). I've had lots of fun playing with it and writing interpreters (in `Racket <https://github.com/dwayne/whitespace-racket>`_, `Haskell <https://github.com/dwayne/whitespace-haskell>`_, `Ruby <https://github.com/dwayne/whitespace-ruby>`_ and now `Python <https://www.python.org/>`_) for it.

Copyright
---------

Copyright (c) 2016 Dwayne Crooks. See `LICENSE </LICENSE.txt>`_ for further details.

.. _Whitespace: https://en.wikipedia.org/wiki/Whitespace_(programming_language)
