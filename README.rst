Whitespace
==========

.. image:: https://img.shields.io/pypi/v/whitespace.svg
    :target: https://pypi.org/project/whitespace/

An interpreter written in `Python <https://www.python.org/>`_ for the imperative, stack-based language called `Whitespace`_.

Installation
------------

To install, simply use pip (or `pipenv`_):

.. code-block:: bash

    $ pip install whitespace

Usage
-----

Let :code:`program.ws` be any `Whitespace`_ program. To execute it, type:

.. code-block:: bash

    $ whitespace program.ws

You can find example `Whitespace`_ programs at `tests/fixtures <https://github.com/dwayne/whitespace-python/tree/master/tests/fixtures>`_.

For example, here's the `factorial program <https://github.com/dwayne/whitespace-python/tree/master/tests/fixtures/fact.ws>`_:

.. code-block:: bash

    $ whitespace fact.ws
    Enter a number: 40
    40! = 815915283247897734345611269596115894272000000000

Development
-----------

Recommended tools:

 - `pyenv <https://github.com/pyenv/pyenv>`_
 - `pipenv`_

Clone the repository and install the dependencies:

.. code-block:: bash

    $ git clone git@github.com:dwayne/whitespace-python.git
    $ cd whitespace-python
    $ pipenv shell
    $ pipenv install --dev

You're now all set to begin development.

Testing
-------

Tests are written using the built-in unit testing framework, `unittest <https://docs.python.org/3/library/unittest.html>`_.

Run all tests.

.. code-block:: bash

    $ python -m unittest

Run a specific test module.

.. code-block:: bash

    $ python -m unittest tests.test_parser

Run a specific test case.

.. code-block:: bash

    $ python -m unittest tests.test_parser.ParserTestCase.test_it_parses_push

References
----------

- `Whitespace tutorial <https://web.archive.org/web/20150618184706/http://compsoc.dur.ac.uk/whitespace/tutorial.php>`_

Credits
-------

Thanks to `Edwin Brady <https://edwinb.wordpress.com/>`_ and Chris Morris for designing/developing this programming language; they are also developers of the `Idris <https://en.wikipedia.org/wiki/Idris_(programming_language)>`_ programming language.

.. _Whitespace: https://en.wikipedia.org/wiki/Whitespace_(programming_language)
.. _pipenv: https://github.com/pypa/pipenv
