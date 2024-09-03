envJSON
=======

.. image:: https://img.shields.io/pypi/v/envjson.svg
    :target: https://pypi.python.org/pypi/envjson
    :alt: PyPI Status

.. image:: https://img.shields.io/travis/mrshu/envjson.svg
    :target: https://travis-ci.org/mrshu/envjson
    :alt: Build Status

.. image:: https://coveralls.io/repos/github/mrshu/envjson/badge.svg?branch=master
    :target: https://coveralls.io/github/mrshu/envjson?branch=master
    :alt: Code coverage Status

.. image:: https://img.shields.io/pypi/l/envjson.svg
   :target: ./LICENSE
   :alt: License Status

``envJSON`` addresses a straightforward challenge: incorporating values from environment variables into JSON configuration files. This functionality is akin to `envyaml <https://github.com/thesimj/envyaml>`_ and `varyaml <https://github.com/abe-winter/varyaml>`_, which offer similar capabilities for YAML, and has significantly inspired this package.

Example
-------

Consider the following configuration saved in ``config.json``:

.. code:: json

  {
    "db": {
      "host": "$DB_HOST",
      "port": "$DB_PORT",
      "username": "$DB_USERNAME",
      "password": "$DB_PASSWORD",
      "name": "my_database"
    }
  }

With the environment variables set as follows:

.. code::

  DB_HOST=some-host.tld
  DB_PORT=3306
  DB_USERNAME=user01
  DB_PASSWORD=veryToughPas$w0rd

This configuration can then be parsed using ``envJSON`` like this:

.. code:: python

  import envjson

  cfg = envjson.load(open('./config.json'))

  print(cfg)
  # {'db': {'host': 'some-host.tld',
  #   'port': 3306,
  #   'username': 'user01',
  #   'password': 'veryToughPas$w0rd',
  #   'name': 'my_database'}}

Tests
-----

This project utilizes `Poetry <https://poetry.eustace.io/>`_. After installation, the tests can be executed by running the following command from the project's root directory:

.. code:: bash

    poetry run nosetests tests

Tests can also be run with `coverage <https://nose.readthedocs.io/en/latest/plugins/cover.html>`_:

.. code:: bash

    poetry run nosetests --with-coverage tests

License
-------

Licensed under the MIT license (see `LICENSE <./LICENSE>`_ file for more details).