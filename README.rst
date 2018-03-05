acidfile
========

`acidfile` module provides the ACIDFile object. This object can be used as a
regular file object but instead of write one copy of the data, it will write
several copies to disk in an ACID manner.

This algorithm was explained by `Elvis Pfützenreuter`_ in his blog post
`Achieving ACID transactions with common files`_.

Latest stable version can be found on `PyPI`_.

.. image:: https://travis-ci.org/nilp0inter/acidfile.png?branch=develop
    :target: https://travis-ci.org/nilp0inter/acidfile

.. image:: https://img.shields.io/pypi/v/acidfile.svg
    :target: https://pypi.python.org/pypi/acidfile
    :alt: Latest PyPI version

`acidfile` is compatible with python 2.6, 2.7, 3.2, 3.3, 3.4 and pypy

Contribute:

.. image:: http://api.flattr.com/button/flattr-badge-large.png
    :target: https://flattr.com/submit/auto?user_id=nilp0inter&url=https://github.com/nilp0inter/acidfile&title=acidfile&language=&tags=github&category=software
    :alt: Flattr this git repo

Installation
------------

Latest version can be installed via `pip`

.. code-block:: bash

   $ pip install --upgrade acidfile


Running the tests
-----------------

Clone this repository and install the develop requirements.

.. code-block:: bash

   $ git clone https://github.com/nilp0inter/acidfile.git
   $ cd acidfile
   $ pip install -r requirements/develop.txt
   $ python setup.py develop
   $ tox


Usage examples
--------------


Basic usage
+++++++++++

.. code-block:: python

   >>> from acidfile import ACIDFile

   >>> myfile = ACIDFile('/tmp/myfile.txt', 'w')
   >>> myfile.write(b'Some important data.')
   >>> myfile.close()

At the close invocation two copies will be written to disk: *myfile.txt.0* and
below *myfile.txt.1*. Each one will have an creation timestamp and a HMAC
signature.

.. code-block:: python

   >>> myfile = ACIDFile('/tmp/myfile.txt', 'r')
   >>> print myfile.read()
   'Some important data.'
   >>> myfile.close()

If any of the files is damaged due to turning off without proper shutdown or
disk failure, manipulation, etc. It will be detected by the internal HMAC and
the other's file data would be used instead.

.. note:: If you want to read an `acidfile`, never pass the full path of the
   real file, instead use the file name that you use in the creation step.

   | ✗ ACIDFile('/tmp/myfile.txt.0', 'r')
   | ✗ ACIDFile('/tmp/myfile.txt.1', 'r')
   | ✓ ACIDFile('/tmp/myfile.txt', 'r')


Context manager
+++++++++++++++

ACIDFile can (and should) be used as a regular context manager:

.. code-block:: python

   >>> with ACIDFile('/tmp/myfile.txt', 'w') as myfile:
   ...     myfile.write(b'Some important data.')


Number of copies
++++++++++++++++

The number of inner copies of the data can be configured through the **copies**
parameter.


Checksum Key
++++++++++++

The key used for compute and check the internal HMAC signature can be setted
by the **key** parameter.

It's recommended to change that key in order to protect against fraud, making
more difficult for a tamperer to put a fake file in place of the legitimate
one.

.. _PyPI: https://pypi.python.org/pypi/acidfile
.. _Elvis Pfützenreuter: epx@epx.com.br
.. _Achieving ACID transactions with common files: http://epx.com.br/artigos/arqtrans_en.php
