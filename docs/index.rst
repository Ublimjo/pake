====
pake
====

**pake** is a replacement of make for python.


Installation
============

**pake** is not yet available in pypi but you can get it from source::

  $ git clone https://github.com/Ublimjo/pake.git
  $ cd pake/
  $ python setup.py install


Difference between make
=======================

+----------------+-------------------------+--------------------------+
|                | make                    | pake                     |
+================+=========================+==========================+
| main file      | Makefile                | _pake_.py                |
+----------------+-------------------------+--------------------------+
| main file type | yaml(yml)               | python(py)               |
+----------------+-------------------------+--------------------------+
|                | .. code-block:: guess   | .. code-block:: python   |
|                |                         |                          |
| declare test   |   test:                 |   def test():            |
|                |       @echo "run test"  |       '''run test'''     |
|                |       pytest            |       x_('pytest')       |
+----------------+-------------------------+--------------------------+


Note
====

This project has been set up using PyScaffold 3.0.3.post0.dev61+ge5fed5a.dirty. For details and usage
information on PyScaffold see http://pyscaffold.org/.


Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changelog>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
