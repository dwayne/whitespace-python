Change Log
----------

`Unreleased`_
+++++++++++++

**Added**

- A change log (guided by http://keepachangelog.com/)
- Notes on installation, usage, development and testing to the README
- A version badge from http://shields.io/
- Begin tracking development dependencies

**Changed**

- Explicitly list the packages to be included in the distribution
- Stop including tests in the distribution
- Stop using ``codecs.open`` since ``open`` does the job in Python 3
- Consistently name test cases with a TestCase suffix

`1.0.0b1`_ (2016-09-02)
+++++++++++++++++++++++

**Added**

- A fully tested parser with error handling and source location tracking
- An interpreter
- A CLI for running the interpreter

**Fixed**

- Fix the console's output buffering by flushing after every write

`0.1.0.dev2`_ (2016-09-01)
++++++++++++++++++++++++++

**Changed**

- Update ``MANIFEST.in`` and ``setup.py`` to ensure the correct files are included in the distribution


`0.1.0.dev1`_ (2016-08-31)
++++++++++++++++++++++++++

**Added**

- A virtual machine
- A console abstraction to make it easier to test I/O
- The stack manipulation, arithmetic, heap access, flow control and I/O instructions

0.0.1.dev1 (2016-08-31)
+++++++++++++++++++++++

Birth!

.. _`Unreleased`: https://github.com/dwayne/whitespace-python/compare/v1.0.0b1...HEAD
.. _`1.0.0b1`: https://github.com/dwayne/whitespace-python/compare/v0.1.0.dev2...v1.0.0b1
.. _`0.1.0.dev2`: https://github.com/dwayne/whitespace-python/compare/v0.1.0.dev1...v0.1.0.dev2
.. _`0.1.0.dev1`: https://github.com/dwayne/whitespace-python/compare/v0.0.1.dev1...v0.1.0.dev1
