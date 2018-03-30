📦 pkg-info
===========

Tiny library to fetch package info from `PyPI <https://pypi.org/>`_.


Install
-------

``pipenv install pkg_info``

or

``pip intall pkg_info``

Usage
-----

.. code-block:: python

    from pkg_info import get_pkg_info

    pkg = get_pkg_info('requests')
    pkg.name        # 'requests'
    pkg.version     # '2.18.4'
    pkg.author.name # 'Kenneth Reitz'
